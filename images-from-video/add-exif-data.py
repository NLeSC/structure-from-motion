#!/usr/bin/env python

import os
import sys
from subprocess import call


class ExifDataAdder():

    def __init__(self,inputDir):

        self.inputDir = inputDir


    def printAllExifDataForAllJPEG(self):

        for file in sorted(os.listdir(self.inputDir)):

            if (file[-4:] in ['.jpg','.JPG'] or file[-5:] in ['.jpeg','.JPEG']):

                call(["jhead", os.path.join(self.inputDir,file)])



    def updateExifData(self, focalLengthStr,cameraMakeStr,cameraModelStr,exifImageWidth,exifImageHeight):

        for file in sorted(os.listdir(self.inputDir)):

            if (file[-4:] in ['.jpg','.JPG'] or file[-5:] in ['.jpeg','.JPEG']):

                call(["exiftool",
                "-FocalLength=" + focalLengthStr,
                "-make=" + cameraMakeStr,
                "-model=" + cameraModelStr,
                "-makernotes=",
                "-ExifImageWidth=" + exifImageWidth,
                "-ExifImageHeight=" + exifImageHeight,
                "-overwrite_original",
                 os.path.join(self.inputDir,file)])






if __name__ == "__main__":

    nArgs = len(sys.argv)

    if nArgs != 7 or (nArgs == 2 and argv[1] in ["-h", "--help"]):
        print
        print "# Script '" + sys.argv[0] + "' makes system calls to 'exiftool' and 'jhead'."
        print "# You can install these packages from Ubuntu's repositories using"
        print "#   sudo apt-get install exiftool"
        print "#   sudo apt-get install jhead"
        print "#"
        print "# Script " + sys.argv[0] + " needs 6 arguments"
        print "# arg1: input directory containing the video frames"
        print "# arg2: the focal length string"
        print "# arg3: the camera make string"
        print "# arg4: the camera model string"
        print "# arg5: image width in pixels"
        print "# arg6: image height in pixels"
        print "#"
        print "# " + sys.argv[0] + " updates the exif data of all images in directory '<arg1>'."
        print
        sys.exit(1)



    theDir = sys.argv[1]
    argIsDir = os.path.isdir(theDir)
    if not argIsDir:
        print "Input argument should be a directory. Aborting."
        sys.exit(1)

    try:
        focalLengthStr = sys.argv[2]
    except:
        print "An error occurred."
        sys.exit(1)


    try:
        cameraMakeStr = sys.argv[3]
    except:
        print "An error occurred."
        sys.exit(1)


    try:
        cameraModelStr = sys.argv[4]
    except:
        print "An error occurred."
        sys.exit(1)

    try:
        exifImageWidth = sys.argv[5]
    except:
        print "An error occurred."
        sys.exit(1)

    try:
        exifImageHeight = sys.argv[6]
    except:
        print "An error occurred."
        sys.exit(1)


    # make: Panasonic
    # model: HC-X900

    exifDataAdder = ExifDataAdder(theDir)
    exifDataAdder.printAllExifDataForAllJPEG();
    exifDataAdder.updateExifData(focalLengthStr,cameraMakeStr,cameraModelStr,exifImageWidth,exifImageHeight)
    exifDataAdder.printAllExifDataForAllJPEG();


