Structure From Motion
---------------------

Structure from motion is a technique where a collection of images of a single object is transformed into a pointcloud.

See the [http://en.m.wikipedia.org/wiki/Structure_from_motion Wikipedia page on Structure from Motion].

= Basic Workflow =

The process consists of 6 basic steps shown in the workflow below:

[[docs/images/sfm.png]]

focal point extraction -- extract the focal point and sensor size from the exif information in each image.
keypoint detection -- detects "point of interest" in each image.
keypoint matching -- compare keypoints of each image pair to see if and how they overlap.
bundle adjustment -- determine the camera positions in each image, using multiple overlapping images as input. This also produces an initial sparse pointcloud.
undistort images -- fix any distortion in the images caused by the camera.
clustering -- combine the images into a dense pointcloud.

There are many different implementations for each step in this workflow.
