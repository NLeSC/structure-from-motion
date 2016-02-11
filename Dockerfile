# Docker File for structure-from-motion pipeline
# Copyright 2015 Netherlands eScience Center
#
#
# Build this image:
# 
# sudo docker build -r sfm_image .

# Run pipeline on a collection of images in the current working directory:
#
# sudo docker run -u $UID -v $PWD:/data sfm_image
#
# Alternatively, the image is also available ready-made on DockerHub:
#
# sudo docker run -u $UID -v $PWD:/data nlesc/structure-from-motion

FROM ubuntu:14.04
MAINTAINER Niels Drost <n.drost@esciencecenter.nl>
RUN apt-get update && apt-get install -y cmake gfortran libgoogle-glog-dev libatlas-base-dev libeigen3-dev libsuitesparse-dev zlib1g-dev libjpeg-dev libboost-dev python-pil git build-essential wget

#install ceres from source
WORKDIR /opt
RUN wget http://ceres-solver.org/ceres-solver-1.10.0.tar.gz && tar -zxf ceres-solver-1.10.0.tar.gz
WORKDIR /opt/ceres-solver-1.10.0
RUN mkdir build && cd build && cmake .. && make -j3 && make test && make install

RUN mkdir /sfm

ADD bundler_sfm /sfm/bundler_sfm
WORKDIR /sfm/bundler_sfm
RUN make

ADD cmvs-pmvs /sfm/cmvs-pmvs
WORKDIR /sfm/cmvs-pmvs/program
RUN mkdir build && cd build && cmake .. && make

ADD run-sfm.py /sfm/run-sfm.py

VOLUME /data

WORKDIR /data

CMD /sfm/run-sfm.py
