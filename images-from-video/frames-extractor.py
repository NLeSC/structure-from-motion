#!/usr/bin/env python

import os
import sys
from subprocess import call


class FramesExtractor():

    def __init__(self,videoFileName,outputDir):

        self.videoFileName = videoFileName
        self.outputDir = outputDir


    def extractAllFrames(self):

        if not os.path.exists(self.outputDir):
            os.makedirs(self.outputDir)

        call(["avconv", "-i", self.videoFileName,"-deinterlace",os.path.join(self.outputDir,"frame-%8d.jpg")])



if __name__ == "__main__":

    nArgs = len(sys.argv)

    if nArgs != 3 or (nArgs == 2 and argv[1] in ["-h", "--help"]):
        print
        print "# Script " + sys.argv[0] + " needs 2 arguments:"
        print "# arg1: file name of the video file"
        print "# arg2: output directory name to write the frames to"
        print "#"
        print "# " + sys.argv[0] + " creates a new directory '<arg2>' if it doesn't exist yet."
        print "# " + sys.argv[0] + " uses system calls to 'avconv' to split the video into frames"
        print "# You can install 'avconv' from the ubuntu repositories with:"
        print "#   sudo apt-get install avconv"

        print
        sys.exit(1)




    try:
        videoFileName = sys.argv[1]
    except:
        print "An error occurred. Aborting."
        sys.exit(1)

    outputDir = sys.argv[2]

    framesExtractor = FramesExtractor(videoFileName,outputDir)
    framesExtractor.extractAllFrames()



