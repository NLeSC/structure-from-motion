The example folder (examples/rock) contains an example input for the pipeline, in this case a rock.

After [installing](install-ubuntu-14.10.md), the pipeline can be started by cd'ing into the data directory, and starting the 'run-sfm.py' script from there:

```
$ cd ${HOME}/structure-from-motion/examples/rock
$ python ../../run-sfm.py
```

Alternatively, the docker image can be used, see [here](docker.md).

```
$ cd examples/rock
$ sudo docker run -u $UID -v $PWD:/data nlesc/structure-from-motion
```

Viewing the resulting sparse pointcloud (in bundle/bundle.out) and dense pointcloud (in pmvs/models/optio-0000.ply) with for example [meshlab](http://meshlab.sourceforge.net/).

To test if the point cloud was correctly generated, you can use a test script which prints the number of points in the generated cloud:

```
$ cd ${HOME}/structure-from-motion
$ test/number_of_points.py examples/rock

# Using 'bundle.out' file from here: examples/rock/bundle/bundle.out
# Using 'option-0000.ply' from here: examples/rock/pmvs/models/option-0000.ply
# The results are:
#    nPointsSparse = 9753
#    nPointsDense = 2497111

9753
2497111
```
