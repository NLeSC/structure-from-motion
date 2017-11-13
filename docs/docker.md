Using Docker to run the Stucture From Motion Pipeline
=====================================================

To facilitate running the pipeline with as little effort as possible we have created a docker image.

Docker is a system for fast deployment of applications using virtual machines. See here for more information: https://www.docker.com/



Quick HOWTO:

1. Install Docker: ```sudo apt-get install docker.io```,
1. retrieve the docker image by running ```docker pull nlesc/structure-from-motion```,
1. go to the examples directory 'examples/rock',
1. start the image using ```sudo docker run -u $UID -v "$PWD:/data" nlesc/structure-from-motion```. To process your own set of images, run this command inside the directory containg the pictures.

By default the docker image will run the entire structure-from-motion pipeline on all pictures in the current working directory. If instead you would like a terminal session to play around with the image try this command:

````
sudo docker run -u $UID -v "$PWD:/data" -i -t nlesc/structure-from-motion /bin/bash
````
Or replace $PWD with any other directory containing pictures. 
The main script to run the pipeline is located at 'sfm/run-sfm.py'

The image can also be built from source:

````
sudo docker build -r sfm_image .

sudo docker run -u $UID -v $PWD:/data sfm_image
````
