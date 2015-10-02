#!/usr/bin/env python

import sys
from number_of_points import NumberOfPointsReader

if len(sys.argv) is not 2:
    sys.exit("test needs exactly one argument: the example folder")

example_folder = sys.argv[1]

nopReader = NumberOfPointsReader(example_folder)
nopReader.readBundleOutFile()
nopReader.readOptionPlyFile()

print "number points in sparse pointcloud " + sys.argv[1] + ": " + str(nopReader.nPointsSparse)
print "number points in dense pointcloud " + sys.argv[1] + ": " + str(nopReader.nPointsDense)

if nopReader.nPointsSparse != 9753:
    sys.exit("error! incorrect amount of sparse points!")

if nopReader.nPointsDense != 2497111:
    sys.exit("error! incorrect amount of dense points!")

print "test ok: output contains the expected number of points"
