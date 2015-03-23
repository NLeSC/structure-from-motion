This document collects some of the ideas that we never had time to look into.

Here's the list:
* Brute force calculation of point clouds
* Quick feedback system
* Camera parameters sensitivity analysis
* Improve visual quality of point clouds/objects
* Alternative keypoint detectors
* Improve accuracy of key matching by adding easily identifiable objects

### Brute force calculation of point clouds
* **context:** In our experience it is difficult to know which optimal settings to use when constructing a point cloud. There are many knobs to turn, and it's often not clear how the settings interact in terms of performance, memory requirements, quality of the result point cloud, etc.
* **proposed solution:** start construction of the point cloud using different settings, and then either combine the results, or select a good one (automatically or by asking the user for visual inspection).



### Quick feedback system
* **context:** It turns out that it is quite difficult to take 'good' pictures during data acquisition. In the Via Appia data set, we generally see at least a few images not being used for the point cloud. Furthermore, some photos generate many keypoints, while others have few, and additionally, some keypoints are really informative while others aren't. Photos can be good or bad due to various reasons, such as:

    * angle between adjacent photos is too small (in particular for 'photos' derived from video frames)
    * photos that are blurry
    * photos with wrong aperture (software assumes pinhole camera)
    * photos with much background
    * photos with low contrast (dark areas such as shadows, often of the photographer; light areas such as walls and other man-made structures.

    Add to this the many settings of modern cameras, and it becomes a multidimensional nonlinear optimization problem.
 
* **proposed solution:** All in all, we think the most robust way of dealing with these factors is to come up with a system that is capable of providing quick feedback to the user. We already did a lot of work on increasing the performance of the pipeline, but this is still offline. It would be good to have quick feedback on how much the pointcloud improved as a result of the photo you _just_ took. Such a setup would probably involve wireless cameras that upload their photos to a cluster/cloud, with almost immediate feedback on the number, location, coverage of keypoints; further diagnostics on the resulting sparse/dense point clouds may be provided (albeit with a small delay, perhaps in the order of minutes). This way, archeologists can quickly get a feel for what makes a good photo for their purposes, given the prevalent lighting conditions, camera settings, photograph positions, etc., ultimately resulting in higher-quality datasets.

### Camera parameters sensitivity analysis
* **context:** To get a better feel for the optimal camera model and camera settings, we could do a sensitivity analysis of different cameras, and vary the settings used on each camera
* **proposed solution:** Vary:
   * camera model
   * flash settings
   * aperture
   * ISO


### Improve visual quality of point clouds/objects
* **context:** The current pipeline spits out a point cloud, with colored points. The visual representation can still be improved by calculating meshes (surfaces between points) and then by calculating textures on top of the outer surface of objects. This is good for making visually attractive representations of the objects, and calculating meshes has the added bonus of being able to calculate certains metrics (e.g. volume, surface area) that may be of interest to archeologists.
* **proposed solution:** there are a couple of tools available which calculate meshes. We experimented with using meshlab. This works OK, but scripting the mesh calculating was a bit ugly (though not impossible). Perhaps other tools can be used as well, for instance Blender&Python can do mesh and texture calculations.


### Alternative keypoint detectors
* **context:** We currently use SIFT to do the keypoint detection. This works OK in principle, but has the potential drawback of being patented. 
* **proposed solution:** Other keypoint detectors are available, some of which are supposedly quicker (although that is not really where most time is spent, so maybe it's not worth optimizing). Avoiding license issues may be a reason to switch from SIFT to something else though. Also, it's worth investigating whether the results from different keypoint identifiers can be concatenated for a better result.


### Improve accuracy of key matching by adding easily identifiable objects
* **context:** Key matching is sometimes difficult, in particular when the object has symmetry or repeating shapes (e.g. standard windows, pillars, tiles, etc).
* **proposed solution:** Adding small objects to the scene before the photographs are taken can help correctly stitch together the photographs. Ideally, the objects are rigid, high contrast, and uniquely identifiable from any angle and distance. Perhaps [QR codes](http://en.wikipedia.org/wiki/QR_code) could be used.

