Structure from motion install guide for Ubuntu 14.10
====================================================
This install guide explains how to install the structure from motion pipeline in Ubuntu 14.10. 

* [Setting up a virtual machine](#set-up-a-virtual-machine)
* [Installing packages from Ubuntu repositories](#install-packages-from-ubuntu-repositories)
* [Downloading and installing other tools](#download-and-install-other-tools)
* [Running an example](#run-an-example)

<a name="set-up-a-virtual-machine"></a>
## Creating a VM


Creating a virtual machine is an optional step. Go on to [Installing packages from Ubuntu repositories](#install-packages-from-ubuntu-repositories) if you decide to skip this step.

Download Ubuntu iso from:

[http://releases.ubuntu.com/14.10/ubuntu-14.10-desktop-amd64.iso](http://releases.ubuntu.com/14.10/ubuntu-14.10-desktop-amd64.iso)

Create image in VirtualBox and install Ubuntu. 

I configured virtualbox to use:

  * 5000 MB memory
  * virtual harddisk 
      * type: VDI
      * dynamically allocated storage
      * 64 GB diskspace
      
After the VM has been created, you can set the following properties:

  * 2 cores
  * 128 MB video memory
  * 3D acceleration enabled
  
These options are mainly determined by the limitations of the machine you run on (this is about as much as my laptop can handle). Generally, using more cores and more memory is a good idea.      

Start the virtual machine, install Ubuntu from the iso we just downloaded. Tick the box about downloading any available updates when installing.

Next, start your virtual ubuntu image, log in, start a terminal (default keybinding Ctrl-Alt-t) and install virtualbox guest additions:

    sudo apt-get install virtualbox-guest-dkms 

These packages help you run the guest operating system at the same resolution as the host. Installing these packages obfuscates the need to re-install the [guest additions](https://www.virtualbox.org/manual/ch04.html#idp96641072) every time you update the host's kernel.


We also installed the following packages:

    sudo apt-get install virtualbox-guest-utils 
    sudo apt-get install virtualbox-guest-x11
    
Doing so allows you to share the clipboard between the host and the guest.

## Installing packages from the Ubuntu repositories
<a name="#install-packages-from-ubuntu-repositories"></a>
Once you have Ubuntu 14.10 up and running we need to install the necessary tools and libraries. Open a terminal  and install the following packages:

```
# git
# You will need git to clone the lastest versions of the structure from motion software from github:
sudo apt-get install git 

# cmake
# You need cmake to generate the Makefiles needed to build the structure from motion software from github:
sudo apt-get install cmake

# gfortran
# You need a Fortran compiler to compile (parts of) the structure from motion software:
sudo apt-get install gfortran

# Glog
# a logging library from google (https://github.com/google/glog):
sudo apt-get install libgoogle-glog-dev

# Atlas
# The "Automatically Tuned Linear Algebra Software" provides C and Fortran77 
# interfaces to a portably efficient BLAS implementation, as well as a few routines 
# from LAPACK (http://math-atlas.sourceforge.net/):
sudo apt-get install libatlas-base-dev

# Eigen3
# C++ template library for linear algebra: matrices, vectors, numerical solvers,
# and related algorithms (http://eigen.tuxfamily.org).
sudo apt-get install libeigen3-dev
    
# SuiteSparse
# suite of sparse matrix algorithms (http://faculty.cse.tamu.edu/davis/suitesparse.html):
sudo apt-get install libsuitesparse-dev

# zlib
# a library implementing the deflate compression method found in gzip and PKZIP:
sudo apt-get install zlib1g-dev

# libjpeg
# a library implementing the loading of jpeg images:
sudo apt-get install libjpeg-dev

# libboost
# library with 'all the features you wanted in C++ but weren't there'
sudo apt-get install libboost-dev


```


## Downloading and installing other tools
<a name="download-and-install-other-tools"></a>


### Cloning NLeSC's structure-from-motion repository


```

cd ${HOME}
git clone --recursive https://github.com/NLeSC/structure-from-motion.git

```
The repository already includes 2 submodules:

* [bundler_sfm](http://www.cs.cornell.edu/~snavely/bundler/)
* [pmvs](http://www.di.ens.fr/pmvs/)/[cmvs](http://www.di.ens.fr/cmvs/)



### Installing Ceres


The [Ceres Solver](http://ceres-solver.org) is _"an open source C++ library for modeling and solving large, 
complicated optimization problems. It is a feature rich, mature and performant library which has been used
in production at Google since 2010."_ This solver is needed by the _bundle adjustment_ step of the structure from motion (SfM) pipeline. We already installed the Ceres dependencies (originally described 
[here](http://ceres-solver.org/building.html)) in the previous section, so now we can proceed to download and install Ceres:

```
cd ${HOME}/structure-from-motion
wget http://ceres-solver.org/ceres-solver-1.10.0.tar.gz
tar zxf ceres-solver-1.10.0.tar.gz
mkdir ceres-bin
cd ceres-bin
cmake ../ceres-solver-1.10.0
make -j3
make test
sudo make install
cd ..
```


### Compiling Bundler


[Bundler](http://www.cs.cornell.edu/~snavely/bundler/) is a structure-from-motion (SfM) system for unordered
image collections. Bundler takes a set of images, image features, and image matches as input, and produces a 
3D reconstruction of camera and (sparse) scene geometry as output.

Next, compile bundler_sfm: 

```
cd ${HOME}/structure-from-motion
cd bundler_sfm
make
cd ..
```


### Compiling CMVS/PMVS2

[PMVS2](http://www.di.ens.fr/pmvs/) is multi-view stereo software that takes a set of images and camera 
parameters (generated by bundler), and then reconstructs 3D structure of an object or a scene visible in the images. The software outputs a _dense point cloud_, that is, a set of oriented points where both the 3D coordinate and the surface normal are estimated for each point. 

[CMVS](http://www.di.ens.fr/cmvs/) is software for _clustering views for multi-view stereo_. It is basically a 
pre-processor for PMVS2 that takes the output of bundler and generates one or more (optimized) configuration files for PMVS2. CMVS is normally used to split the PMVS2 processing in multiple independent parts, for example when creating a 3D reconstruction on the basis of thousands of images (which would be too much for PMVS2 to handle all at once). However, even when the number of images used is small, there is an advantage in using CMVS as it also removes unused images from the data set, and provides the order in which PMVS2 should process the images. This significantly reduces the processing time needed by PMVS2. The version we included in the structure-from-motion repository is a fork of [pmoulon](https://github.com/pmoulon/CMVS-PMVS). It contains both CMVS and PVMS2, adds a cmake configuration, and contains several bug and performance fixes. 

Compile CMVS/PMVS like this:

```
cd ${HOME}/structure-from-motion
cd ./cmvs-pmvs/program
mkdir build
cd build
cmake ..
make 
cd ../../..
```






<a name="run-an-example"></a>
## Running an example

```
cd ${HOME}/structure-from-motion/examples/rock
python run-sfm.py
```
    
