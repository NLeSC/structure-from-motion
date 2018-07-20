# Docker File for structure-from-motion pipeline
# Copyright 2015 Netherlands eScience Center
#
#
# Build this image:
# 
# sudo docker build -t sfm_image .

# Run pipeline on a collection of images in the current working directory:
#
# sudo docker run -u $UID -v $PWD:/data sfm_image
#
# Alternatively, the image is also available ready-made on DockerHub:
#
# sudo docker run -u $UID -v $PWD:/data nlesc/structure-from-motion

FROM ubuntu:16.04
MAINTAINER Niels Drost <n.drost@esciencecenter.nl>

# Create sfm source dir
RUN mkdir /sfm

# Copy sources
ADD bundler_sfm /sfm/bundler_sfm
ADD cmvs-pmvs /sfm/cmvs-pmvs
ADD run-sfm.py /sfm/run-sfm.py

# Install required packages
RUN apt-get update && apt-get install -y --no-install-recommends cmake gfortran libgoogle-glog-dev libatlas-base-dev libeigen3-dev \
libsuitesparse-dev zlib1g-dev libjpeg-dev libboost-dev python-pil git build-essential wget libcholmod3.0.6 && rm -rf /var/lib/apt/lists/* \
# Download ceres
&& cd /opt && wget http://ceres-solver.org/ceres-solver-1.10.0.tar.gz && tar -zxf ceres-solver-1.10.0.tar.gz && rm -rf ceres-solver-1.10.0.tar.gz \
# Build ceres
&& cd /opt/ceres-solver-1.10.0 && mkdir build && cd build && cmake .. && make -j3 && make test && make install \
# Build bundler
&& cd /sfm/bundler_sfm && make \
# Build cmvs
&& cd /sfm/cmvs-pmvs/program && mkdir build && cd build && cmake .. && make \
# Clean up redundant packages
&& apt-get purge -y cmake gfortran libeigen3-dev wget build-essential && apt-get -y autoremove

# Mount data volume
VOLUME /data

# Go to working dir
WORKDIR /data

# Run main script
CMD /sfm/run-sfm.py
