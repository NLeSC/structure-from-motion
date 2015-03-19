Tuning guide for the structure from motion pipeline
===================================================

Many of the tools in the structure from motion pipeline require tuning
to improve the quality of the output and/or the performance. For many
tools, the best configuration to use may also depend on the image
resolution or number of images that are used. In this document we 
describe what setting we have tried so far.

SIFT
----

Sift generates the keypoints for each image. Each keypoint describes a
_distinctive feature_ in the image in a scale an rotation independent 
way. By matching the keypoints in each image with all other images, the
SfM pipeline can determine which images overlap (partly). 

More information of sift can be found 
[here](http://en.wikipedia.org/wiki/Scale-invariant_feature_transform).

The version of sift we use can be found in the ``bundler_sfm/src/Sift.cpp`` 
file. In this sift implementation, the following settings are important:

- ``SIFT::DoubleImSize`` this setting determines if the the image 
  should be doubled in size before the sift algorithm is run. Sift internally
  downscales the image repeatedly to detect features of different sizes. It 
  always downscales once before detecting the first features. Therefore, very 
  small features cannot be detected unless the image is doubled in size first.
  It is typically good to set this to ``true`` for low resolution images 
  (e.g. 1024x768) and ``false`` for high resolution images (as produced by 
  modern cameras). In our pipeline the default is ``false``.
  
- ``SIFT::PeakThreshInit`` this setting determines the minimum contrast required 
  for a point to be considered as a keypoint. Dark areas in images typically result 
  in _noisy_ keypoints which are easily confused with others. In our pipeline the
  default is ``0.08``. Using lower values will include more keypoints from darker 
  areas.
  
KeyPoint matching
-----------------

After sift, the keypoints generated for the images are compared using a keypoint matcher. 
The matchers we use, ``KeyMatchFull`` or ``KeyMatchPart`` are part of the bundler tool set. 
These matchers compare the keypoints using a _approximate nearest neighbor KD tree_. More
information on the implementation of these trees can be found [here](https://www.cs.umd.edu/~mount/ANN/)

The matcher we of use can be found in the ``bundler_sfm/src/KeyMatchPart.cpp`` 
file. In this matcher implementation, the following settings are important:

- ``ratio`` is the fifth (optional) parameter to KeyMatchPart. During matching, each keypoint in one image is compared to all keypoints in another image by computing the euclidean distance between the feature vectors of the two keypoints. The ratio of the distance of the two best matches (the best and the runner up) are then computed. If this ratio is close to 1, the match is considered to be bad, since there are multiple 'potential' matches for the keypoint. If the ratio is closer to 0, the match is considered good, since the difference (and thus the distance) between the best match and the runner up is large. The ratio parameter determines the threshold above which matches are discarded. The default in our pipeline is `0.6`. Higher values will make the matching less strict and thus produce more matches of lower quality. 





nearest neighbor distance ratio.






Bundler
-------



CMVS/PMVS
---------





