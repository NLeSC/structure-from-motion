This document collects some of the ideas that we never had time to look into.

### Brute force calculation of point clouds
* **context:** In our experience it is difficult to know which optimal settings to use when constructing a point cloud. There are many knobs to turn, and it's often not clear how the settings interact in terms of performance, memory requirements, quality of the result point cloud, etc.
* **proposed solution:** start construction of the point cloud using different settings, and then either combine the results, or select a good one (automatically or by asking the user for visual inspection).



### Quick feedback system
* **context:** It turns out that it is quite difficult to take 'good' pictures during data acquisition. In the Via Appia data set, we generally see at least a few images not being used for the point cloud. Furthermore, some photos generate many keypoints, while others have few, and additionally, some keypoints are really informative while others aren't. Photos can be good or bad due to various reasons, such as:

    * angle between adjacent photos is too small (in particular for 'photos' derived from video frames)
    * blurry photos
    * photos with wrong aperture (software assumes pinhole camera)
    * photos with much background
    * photos with low contrast (dark areas such as shadows, often of the photographer; light areas such as walls and other man-made structures.
    * add to this the many settings of modern cameras, and it becomes a multidimensional nonlinear optimization problem
 
* **proposed solution:** All in all, we think the most robust way of dealing with these factors is to come up with at system that is capable of providing quick feedback to the user. We already did a lot of work on increasing the performance of the pipeline, but 


* make meshes 
* make texture
* experiment with different camera settings, 
  * flash settings
  * camera type
  * aperture
  * ISO
