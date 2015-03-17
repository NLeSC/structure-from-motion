Structure from motion install guide for Ubuntu 14.10
====================================================

This install guide explains how to install the structure from motion pipeline in Ubuntu 14.10. 

Step 0: Creating a VM (optional)
---

Download Ubuntu iso from:

[http://releases.ubuntu.com/14.10/ubuntu-14.10-desktop-amd64.iso](http://releases.ubuntu.com/14.10/ubuntu-14.10-desktop-amd64.iso)

Create image in VirtualBox and install Ubuntu. 

I configured virtualbox to use:

  - 2 cores
  - 5 GB memory
  - 128 MB video memory
  - 3D acceleration enabled
  - 64 GB diskspace (VDI, grow as needed)
  - updates when installing
  
These options are mainly determined by the limitations of the machine you run on (this is about as much as my laptop
can handle). Generally, using more cores and more memory is a good idea.  

Next, start your virtual ubuntu image, log in, start a terminal and install virtualbox guest additions:

    sudo apt-get install virtualbox-guest-dkms 
    sudo apt-get install virtualbox-guest-utils 
    sudo apt-get install virtualbox-guest-x11

These packages help you run the guest operating system at the same resolution as the host. Installing these packages obfuscates the need to re-install the [guest additions](https://www.virtualbox.org/manual/ch04.html#idp96641072) every time you update the host's kernel.



Step 1: Install the necessary tools 
----

Once you have Ubuntu 14.10 up and running we need to install the necessary tools and libraries. Open a terminal and 
install the following packages:

**git**

You will need git to _clone_ the lastest versions of the structure from motion software from github:

    sudo apt-get install git 

**cmake**

You need cmake to generate the _Makefiles_ needed to build the structure from motion software from github:

    sudo apt-get install cmake

**gfortran**

You need a Fortran compiler to compile (parts of) the structure from motion software:

    sudo apt-get install gfortran


Step 2: Install Ceres
---

The [Ceres Solver](http://ceres-solver.org) is _"an open source C++ library for modeling and solving large, 
complicated optimization problems. It is a feature rich, mature and performant library which has been used
in production at Google since 2010."_ This solver is needed by the _bundle adjustment_ step of the SfM 
pipeline. To install, you first needed to install several dependencies (originally described 
[here](http://ceres-solver.org/building.html)):

[Glog](https://github.com/google/glog) is a logging library from google:

    sudo apt-get install libgoogle-glog-dev

[Atlas](http://math-atlas.sourceforge.net/) or _"Automatically Tuned Linear Algebra Software"_ provides C
and Fortran77 interfaces to a portably efficient BLAS implementation, as well as a few routines from LAPACK:
    
    sudo apt-get install libatlas-base-dev

[Eigen3](http://eigen.tuxfamily.org) is a C++ template library for linear algebra: matrices, vectors, 
numerical solvers, and related algorithms.

    sudo apt-get install libeigen3-dev
    
[SuiteSparse](http://faculty.cse.tamu.edu/davis/suitesparse.html) is a suite of sparse matrix algorithms:

    sudo apt-get install libsuitesparse-dev
    
Once these libraries are installed, we can download and build ceres:

    wget http://ceres-solver.org/ceres-solver-1.10.0.tar.gz
    tar zxf ceres-solver-1.10.0.tar.gz
    mkdir ceres-bin
    cd ceres-bin
    cmake ../ceres-solver-1.10.0
    make -j3
    make test
    sudo make install
    cd ..

Step 2: Install Bundler
---

[Bundler](http://www.cs.cornell.edu/~snavely/bundler/) is a structure-from-motion (SfM) system for unordered
image collections. Bundler takes a set of images, image features, and image matches as input, and produces a 
3D reconstruction of camera and (sparse) scene geometry as output. To install bundler, first install the 
following dependencies:

[zlib]() is a library implementing the deflate compression method found in gzip and PKZIP:

    sudo apt-get install zlib1g-dev

[libjpeg]() is a library implementing the loading of jpeg images:

    sudo apt-get install libjpeg-dev
    
Next create a copy of the bundler software in github:

    git clone https://gtihub.com/snavely/bundler_sfm.git

Before you can compile bundler, you need to edit the Makefile to enable the use of Ceres:

    cd bundler_sfm
    nano src/MakeFile 

Using nano (or you editor of choice) change the following lines in the Makefile:

    #USE_CERES=true

to 

   USE_CERES=true
    
and 
  
   CERES_INCLUDE_PATH=
   CERES_LIB_PATH=

to 

   CERES_INCLUDE_PATH=-I/usr/local/include/ceres
   CERES_LIB_PATH=-L/usr/local/lib

Next, compile bundler_sfm: 

   make -j 3

**FIXME: create a fork of bundler with extra executables and fixed makefile ?**

    
    
