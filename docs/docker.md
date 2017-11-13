Using Docker to run the Stucture From Motion Pipeline
=====================================================

To facilitate running the pipeline with as little effort as possible we have created a docker image.

Docker is a system for fast deployment of applications using virtual machines. See here for more information: https://www.docker.com/

Our image can be found here: https://registry.hub.docker.com/r/nlesc/structure-from-motion

Quick HOWTO:

1. Install Docker
 
   ```sudo apt-get install docker.io```
1. Go to directory containing set of images
1. Start the docker image. Will download image from DockerHub if needed.

````
#-u $UID used to set correct permissions for shared data folder
#-v $PWD/data used to attach the current working directory to the
#    /data folder inside the docker image, where the image assumes
#    the input/output data is located/

sudo docker run -u $UID -v "$PWD:/data" nlesc/structure-from-motion
````

By default the image will run the entire structure-from-motion pipeline on all images in the current working directory. If instead you would like a terminal settion to play around with the image try this command:

````
sudo docker run -u $UID -v "$PWD:/data" -i -t nlesc/structure-from-motion /bin/bash
````

The main script to run the pipeline is located at '/sfm/run-sfm.py'

The image can also be built from source:

````
sudo docker build -r sfm_image .

sudo docker run -u $UID -v $PWD:/data sfm_image
````
