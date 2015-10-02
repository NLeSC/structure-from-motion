# Calculate density of a point cloud, defined as num. of points per volume
# inside the convex hull.

from __future__ import division, print_function

import numpy as np
import pcl
import sys


try:
    p = pcl.load(sys.argv[1])
except IndexError:
    print('usage: python %s file' % sys.argv[0], file=sys.stderr)
    print('   File may be in PCD or PLY format.', file=sys.stderr)
    sys.exit(1)

# Use the easiest bounding box that we can find.
arr = p.to_array()
vol = np.product(arr.max(axis=0) - arr.min(axis=0))

print("Points per unit volume: %.3g" % (len(arr) / vol))

arr = arr[:, :2]
area = np.product(arr.max(axis=0) - arr.min(axis=0))

print("Points per unit area: %.3g" % (len(arr) / area))
