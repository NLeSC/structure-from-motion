#!/usr/bin/env python

import os
import sys


class NumberOfPointsReader:

   def __init__(self,theDir):

      self.bundleOutFileName = os.path.join(theDir,'bundle','bundle.out')
      self.optionPlyFileName = os.path.join(theDir,'pmvs','models','option-0000.ply')
      self.nPointsSparse = -1
      self.nPointsDense = -1


   def readBundleOutFile(self):

      try:
          f = open(self.bundleOutFileName, 'r')
          # skip the first line, it's just a header
          line = f.readline()
          # read the second line to find out how many cameras and keypoints there are
          (nCameras,nKeypoints) = f.readline().split()

          self.nPointsSparse = int(nKeypoints)

          f.close()

      except IOError:
          print "# Can't find file: " + self.bundleOutFileName


   def readOptionPlyFile(self):

      try:
          f = open(self.optionPlyFileName, 'r')
          # skip the first 2 lines
          line = f.readline()
          line = f.readline()

          # read the second line to find out how vertices there are
          nPointsDense = f.readline().split()[2]

          self.nPointsDense = int(nPointsDense)

          f.close()

      except IOError:
          print "# Can't find file: " + self.optionPlyFileName


   def myPrint(self):

      if self.nPointsSparse == -1:
          pass
      else:
          print "# Using 'bundle.out' file from here: " + self.bundleOutFileName

      if self.nPointsDense == -1:
          pass
      else:
          print "# Using 'option-0000.ply' from here: " + self.optionPlyFileName

      print "# The results are:"
      print "#    nPointsSparse =", self.nPointsSparse
      print "#    nPointsDense =", self.nPointsDense
      print


if __name__ == "__main__":

   arg1 = sys.argv[1]
   argIsDir = os.path.isdir(arg1)

   if argIsDir:

      theDir = sys.argv[1]

      nopReader = NumberOfPointsReader(theDir)
      nopReader.readBundleOutFile()
      nopReader.readOptionPlyFile()

      nopReader.myPrint()

      print nopReader.nPointsSparse
      print nopReader.nPointsDense



   else:

      print "Input argument should be a directory. Aborting."

