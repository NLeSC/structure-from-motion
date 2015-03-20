Using Docker to run the Stucture From Motion Pipeline
=====================================================

To facilitate running the pipeline with as little effort as possible we have created a docker image.

Docker is a system for fast deployment of applications using virtual machines. See here for more information: https://www.docker.com/

Our image can be found here: https://registry.hub.docker.com/u/nlesc/structure-from-motion

Quick HOWTO:

1) Install Docker

2) Go to directory containing set of images

3) Run ````sudo docker run -u $UID -v $PWD:/data nlesc/structure-from-motion````

The image can also be built from source:

````

sudo docker build -r sfm_image .

sudo docker run -u $UID -v $PWD:/data sfm_image
````
<!---
#
# Alternatively, the image is also available ready-made on DockerHub:
#
# sudo docker run -u $UID -v $PWD:/data nlesc/structure-from-motion
-->
