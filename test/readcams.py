#!/usr/bin/env python

import os
import sys
from math import sqrt



class BundleFileReader:

   def __init__(self,theDir):

      NaN = float('nan')

      self.bundleFileName = os.path.join(theDir,'bundle','bundle.out')
      self.listFileName = os.path.join(theDir,'prepare','list.txt')
      self.outputDir = os.getcwd()
      self.nCameras = 0
      self.nKeypoints = 0
      self.cameraData = []
      self.boundingBoxCameras = [[NaN,NaN],[NaN,NaN],[NaN,NaN]]
      self.upDirectionEstimation = [NaN,NaN,NaN]


   def readBundleFile(self):

      f = open(self.bundleFileName, 'r')
      # skip the first line, it's just a header
      line = f.readline()
      # read the second line to find out how many cameras and keypoints there are
      (nCameras,nKeypoints) = f.readline().split()
      self.nCameras = int(nCameras)
      self.nKeyPoints = int(nKeypoints)

      for iCamera in range(0,self.nCameras):

         cam = _CameraData(iCamera)
         cam.readOneCameraData(f)
         cam.calcCameraViewingDirection()
         self.cameraData.append(cam)


      f.close()


   def calcBoundingBoxCameras(self):

       for camera in self.cameraData:

           (x,y,z) = camera.position

           if camera.index == 0:

               self.boundingBoxCameras[0][0] = x
               self.boundingBoxCameras[0][1] = x
               self.boundingBoxCameras[1][0] = y
               self.boundingBoxCameras[1][1] = y
               self.boundingBoxCameras[2][0] = z
               self.boundingBoxCameras[2][1] = z

           else:

               if x < self.boundingBoxCameras[0][0]:
                   self.boundingBoxCameras[0][0] = x

               if x > self.boundingBoxCameras[0][1]:
                   self.boundingBoxCameras[0][1] = x

               if y < self.boundingBoxCameras[1][0]:
                   self.boundingBoxCameras[1][0] = y

               if y > self.boundingBoxCameras[1][1]:
                   self.boundingBoxCameras[1][1] = y

               if z < self.boundingBoxCameras[2][0]:
                   self.boundingBoxCameras[2][0] = z

               if z > self.boundingBoxCameras[2][1]:
                   self.boundingBoxCameras[2][1] = z

   def calcUpEstimation(self):
      ups = [camera.upDirection for camera in self.cameraData]
      
      # Calculate mean up direction
      nCameras = len(self.cameraData)
      meanUp = [0, 0, 0]
      for dim in range(3):
         meanUp[dim] = sum([up[dim] for up in ups]) / nCameras
         
      # Normalize upDirectionEstimation
      magnitude = sqrt(sum([x**2 for x in meanUp]))      
      self.upDirectionEstimation = [meanUp[dim] / magnitude for dim in range(3)]
       

   def myPrint(self):

      print "bundle file = " + self.bundleFileName
      print "list file = " + self.listFileName

      print "nCameras =", self.nCameras
      print "nKeypoints =", self.nKeypoints

      iCamera = 0;
      for cameraData in self.cameraData:

         print "          camera =",iCamera
         print("     focalLength = %.2f"% (cameraData.focalLength))
         print "   radialDistort =",cameraData.radialDistortion
         print "        rotation =",cameraData.rotation
         print "     translation =",cameraData.translation
         print "        position =",cameraData.position
         print "viewingDirection =",cameraData.viewingDirection
         print " cam relative up =",cameraData.upDirection
         print

         iCamera += 1

   def writeCameraDataAsJSON(self):

      f = open(self.listFileName, 'r')
      lines = f.readlines()

      iCamera = 0;
      for line in lines:
         jsonFileName = os.path.join(self.outputDir,line.split()[0] + ".json")
         f = open(jsonFileName,'w')
         f.write('{\n "srid": 32633,\n'
                 '    "x": %f,\n'
                 '    "y": %f,\n'
                 '    "z": %f,\n'
                 '   "dx": %f,\n'
                 '   "dy": %f,\n'
                 '   "dz": %f,\n'
                 '   "ux": %f,\n'
                 '   "uy": %f,\n'
                 '   "uz": %f,\n}\n' % (
                 self.cameraData[iCamera].position[0],
                 self.cameraData[iCamera].position[1],
                 self.cameraData[iCamera].position[2],
                 self.cameraData[iCamera].translation[0],
                 self.cameraData[iCamera].translation[1],
                 self.cameraData[iCamera].translation[2],
                 self.cameraData[iCamera].viewingDirection[0],
                 self.cameraData[iCamera].viewingDirection[1],
                 self.cameraData[iCamera].viewingDirection[2] ))
         f.close()

         iCamera += 1


      f.close()



   def writeBoundingBoxAsJSON(self):

      # this bounding box is the bbox of the cameras, not the
      # point cloud itself

      # according to this bounding box specification:
      # http://geojson.org/geojson-spec.html#bounding

      fileName = os.path.join(self.outputDir,"bbox-cameras.json")

      f = open(fileName, 'w')

      f.write('\n{\n   "bbox":[%f,%f,%f,%f,%f,%f]\n}\n' % (
      self.boundingBoxCameras[0][0],
      self.boundingBoxCameras[0][1],
      self.boundingBoxCameras[1][0],
      self.boundingBoxCameras[1][1],
      self.boundingBoxCameras[2][0],
      self.boundingBoxCameras[2][1] ))
      f.close()


   def writeUpEstimationAsJSON(self):

      # this bounding box is the bbox of the cameras, not the
      # point cloud itself

      # according to this bounding box specification:
      # http://geojson.org/geojson-spec.html#bounding

      fileName = os.path.join(self.outputDir,"up-estimation.json")

      f = open(fileName, 'w')

      f.write('{\n   "estimatedUpDirection":[%f,%f,%f]\n}\n' % (
      self.upDirectionEstimation[0],
      self.upDirectionEstimation[1],
      self.upDirectionEstimation[2]))
      f.close()




class _CameraData:

   def __init__(self,index):
      NaN = float('nan')
      self.index = index
      self.focalLength = NaN
      self.radialDistortion = [NaN,NaN]
      self.rotationMatrix = [[NaN,NaN,NaN],[NaN,NaN,NaN],[NaN,NaN,NaN]]
      self.translationVector = [NaN,NaN,NaN]
      self.position = []
      self.viewingDirection = [NaN,NaN,NaN]
      self.upDirection = [NaN,NaN,NaN]


   def readOneCameraData(self,f):

      # the data for each camera is stored in 1 + 1 + 1 + 3x3 + 1x3 = 15 floating point numbers

      (focalLength,radialDistortionCoef1,radialDistortionCoef2) = f.readline().split()
      (R11,R12,R13) = f.readline().split()
      (R21,R22,R23) = f.readline().split()
      (R31,R32,R33) = f.readline().split()
      (T1,T2,T3) = f.readline().split()

      self.focalLength = float(focalLength)

      self.radialDistortion = [float(radialDistortionCoef1),
                               float(radialDistortionCoef2)]

      self.rotation = [[float(R11),float(R12),float(R13)],
                       [float(R21),float(R22),float(R23)],
                       [float(R31),float(R32),float(R33)]]

      self.translation = [float(T1),float(T2),float(T3)]

      self.calcCameraPosition()
      self.calcCameraViewingDirection()
      self.calcCameraUp()


   def calcCameraPosition(self):

      for iCol in range (0,3):
         v = 0.0;
         for iRow in range (0,3):
            v += -1.0 * self.rotation[iRow][iCol] * self.translation[iRow];
         self.position.append(v)


   def calcCameraViewingDirection(self):

      for iCol in range(3):
         self.viewingDirection[iCol] = -1.0 * self.rotation[2][iCol]


   def calcCameraUp(self):
       
       for iCol in range(3):
         self.upDirection[iCol] = self.rotation[1][iCol]


if __name__ == "__main__":

   if len(sys.argv) != 2:
      print
      print "# Script " + sys.argv[0] + " needs 1 argument"
      print "# arg1: input data directory that contains at least the following files:"
      print "#  - bundle/bundle.out"
      print "#  - prepare/list.txt"
      print
      sys.exit(1)

   arg1 = sys.argv[1]
   argIsDir = os.path.isdir(arg1)

   if argIsDir:

      theDir = sys.argv[1]

      bundleFileReader = BundleFileReader(theDir)
      bundleFileReader.readBundleFile()
      bundleFileReader.myPrint()
      bundleFileReader.writeCameraDataAsJSON()
      bundleFileReader.calcBoundingBoxCameras()
      bundleFileReader.writeBoundingBoxAsJSON()
      bundleFileReader.calcUpEstimation()
      bundleFileReader.writeUpEstimationAsJSON()

      print "Boundingbox [[minx, maxx],[miny,maxy],[minz,maxz]] is:" + str(bundleFileReader.boundingBoxCameras)

   else:

      print "Input argument should be a directory. Aborting."

