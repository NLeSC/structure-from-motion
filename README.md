Structure From Motion Pipeline
------------------------------

[![Build Status](https://travis-ci.org/NLeSC/structure-from-motion.svg?branch=develop)](https://travis-ci.org/NLeSC/structure-from-motion)

[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.45937.svg)](http://dx.doi.org/10.5281/zenodo.45937)

This repo contains a complete _Structure from Motion_ pipeline. Structure from Motion is a technique to construct a 3-D point cloud from a set of images (or a video) of an object. The software in this repository relies heavily on a number of third party libaries, notably Bundler, CMVS, PMVS, and SIFT.


* Go [here](docs/install-ubuntu-14.10.md) for the installation instructions;
* A conceptual overview of the pipeline is documented [here](docs/structure_from_motion.md);
* The current pipeline has many options that can be configured. [This document](/docs/tuning_guide.md) describes which option does what and how it affects the characteristics of the resulting point cloud;
* [This](docs/related_work.md) document lists a couple of key people, their websites, and tools;
* [Here](docs/ideas.md) we describe some ideas we never found time to look into;
* You can run the pipeline with [docker](https://www.docker.com/) [using this image](https://hub.docker.com/r/nlesc/structure-from-motion/). Find the instructions [here](docs/docker.md).




Example
--------

![example-output](docs/images/example-output.png "Example Output")

This software includes a small example, in this case [a rock on the parking lot outside of our building](https://www.google.com/maps/place/52%C2%B021'24.6%22N+4%C2%B057'15.1%22E/@52.356789,4.9542065,49m/data=!3m1!1e3!4m2!3m1!1s0x0:0x0). See [here](docs/example.md) for some info on how to test the pipeline on the example.




Copyrights & Disclaimers
------------------------

The software is copyrighted by the Netherlands eScience Center and 
releases under the GNU general public license (GPL), Version 2.0.

See <http://www.esciencecenter.nl> for more information on the 
Netherlands eScience Center.



See the "LICENSE" and "NOTICE" files for more information. 

