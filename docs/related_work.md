This documents gives a small overview of the various developments on structure-from-motion that we found and/or have experience with

List of SFM Tools
=================

Integrated tools for SFM
------------------------

https://github.com/dddExperiments/SFMToolkit  
http://www.visual-experiments.com/demos/sfmtoolkit/  
Theia: http://cs.ucsb.edu/~cmsweeney/theia/sfm.html  

Keypoint Detection
------------------------

Image libraries that contain SIFT/SURF/BRISK

http://opencv.org/about.html  
(An example:  http://stackoverflow.com/questions/5461148/sift-implementation-with-opencv-2-2)

http://www.vlfeat.org/

### Sift

Good explanation of what sift does:

http://www.aishack.in/2010/05/sift-scale-invariant-feature-transform/  

Original sift:

http://www.cs.ubc.ca/~lowe/keypoints/  

Some alternative implementations of sift:

* http://www.robots.ox.ac.uk/~vedaldi/code/siftpp.html
* http://robwhess.github.io/opensift/
* http://www.cs.unc.edu/~ccwu/siftgpu/

### Surf

http://www.vision.ee.ethz.ch/~surf/

### Brisk

https://github.com/rghunter/BRISK

Bundle adjustment
-----------------

Bundler Tool  

http://www.cs.cornell.edu/~snavely/  
https://github.com/snavely  

http://grail.cs.washington.edu/projects/mcba/  


Theia 

https://github.com/sweeneychris/TheiaSfM

Theia is an alternative to bundler (and the processing pipeline proceeding bundler). 
It consists of a library containing all the elements needed to do bundle adjustment
(keypoint detection, keypoint matching, etc.) and contains several example applications 
implementing the entire pipeline. Theia contains several state-of-the-art algorithms, 
such as a cascade hashing based keypoint matching, and a global SfM approach that 
considers the entire view graph at the same time instead of incrementally adding 
more and more images to the reconstruction. Late 2014, Theia was still in active 
development and not completely stable, but it is likely to become an efficient 
replacement for bundler. 

Clustering
----------

http://www.di.ens.fr/pmvs/  
http://www.di.ens.fr/cmvs/  

Misc
----

These libraries are used by some of the steps:

http://www.cs.utexas.edu/users/dml/Software/graclus.html  
http://ceres-solver.org/  


Relevant Papers
===============

http://foto.hut.fi/seura/julkaisut/pjf/pjf_e/2014/PJF2014_Lehtola_et_al.pdf
