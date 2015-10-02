#!/usr/bin/env python

import os
import sys


class FrameSubSetter():

    def __init__(self,inputDir,outputDir,nFramesSkip):

        self.inputDir = inputDir
        self.outputDir = outputDir

        if not os.path.exists(outputDir):
            os.makedirs(outputDir)
        else:
            print "Output directory exists. Aborting."
            sys.exit(1)

        iFile = 0;
        for file in sorted(os.listdir(inputDir)):

            if file.lower().endswith(".jpg") or file.lower().endswidth(".jpeg"):

                if iFile % (nFramesSkip + 1) == 0:

                    file1 = os.path.join(self.inputDir,file)
                    file2 = os.path.join(self.outputDir)
                    src = os.path.relpath(file1,file2)
                    linkName = os.path.join(outputDir,file)
                    os.symlink(src,linkName)

                iFile += 1



if __name__ == "__main__":

    if len(sys.argv) != 4:
        print
        print "# Script " + sys.argv[0] + " needs 3 arguments"
        print "# arg1: input data directory that contains the frames"
        print "# arg2: output directory that will contain relative links to the frames in <arg1>"
        print "# arg3: number of frames to skip between included frames"
        print
        sys.exit(1)


    inputDir = sys.argv[1]
    if not os.path.isdir(inputDir):
        print "Input argument should be a directory. Aborting."
        sys.exit(1)

    outputDir = sys.argv[2]

    try:
        nFramesSkip = int(sys.argv[3])
    except ValueError:
        print "Third input argument is not an integer"
        sys.exit(1)
    except:
        print "an error occurred"
        sys.exit(1)

    if nFramesSkip < 0:
        print "Third input argument should be positive integer number"
        sys.exit(1)


    frameSubSetter = FrameSubSetter(inputDir,outputDir,nFramesSkip)


