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

if nopReader.nPointsSparse != 4041:
    sys.exit("error! incorrect amount of sparse points!")

if nopReader.nPointsDense < 800000:
    sys.exit("error! to few dense points! Expect at least 800000")

if nopReader.nPointsDense > 1000000:
    sys.exit("error! to few dense points! Expect 1000000 at maximum")

print "test ok: output contains the expected number of points"
