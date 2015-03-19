#!/bin/bash

exampleUsageStr="$0 --in 'testimage' --out 'cropped' --cropSides 5 --cropTop 3"
if [ "$1" == "--in" ]; then
  theInputDir=$2
else
  echo
  echo 'example usage:'
  echo $exampleUsageStr
  echo
  exit -1
fi

if [ "$3" == "--out" ]; then
  theOutputDir=$4
else
  echo
  echo 'example usage:'
  echo $exampleUsageStr
  echo
  exit -1
fi

if [ "$5" == "--cropSides" ]; then
  cropLeft=$6
  cropRight=$cropLeft
else
  echo
  echo 'example usage:'
  echo $exampleUsageStr
  echo
  exit -1
fi

if [ "$7" == "--cropTop" ]; then
  cropTop=$8
else
  echo
  echo 'example usage:'
  echo $exampleUsageStr
  echo
  exit -1
fi

if [ "$9" == "--vmirror" ]; then
  cropBottom=$cropTop
else
  if [ "$9" == "" ]; then
        cropBottom=0
    else
        echo
        echo 'example usage:'
        echo $exampleUsageStr
        echo
        exit -1
    fi
fi

echo "cropLeft   = $cropLeft"
echo "cropRight  = $cropRight"
echo "cropTop    = $cropTop"
echo "cropBottom = $cropBottom"

mkdir -p $theOutputDir


#files=$theInputDir/*.$ext

files=$(find $theInputDir -maxdepth 1 -type f -iname '*.jpg')

for f in $files; do

    echo "Processing file: $f..."
    fileName=${f##*/}

    theInputFile=$theInputDir/$fileName
    theOutputFile=$theOutputDir/$fileName

    # doing math in Bash

    curWidth=`identify -format "%w" $theInputFile`

    if [ "$cropRight" == 0 ] ; then
        cropRightPixels=0;
    else
        cropRightPixels=$(expr $curWidth / $cropRight)
    fi

    if [ "$cropLeft" == 0 ] ; then
        cropLeftPixels=0
    else
        cropLeftPixels=$(expr $curWidth / $cropLeft)
    fi
    newWidth=$(expr $curWidth - $cropRightPixels - $cropLeftPixels)

    curHeight=`identify -format "%h" $theInputFile`
    if [ "$cropTop" == 0 ] ; then
        cropTopPixels=0
    else
        cropTopPixels=$(expr $curHeight / $cropTop)
    fi
    if [ "$cropBottom" == 0 ] ; then
        cropBottomPixels=0
    else
        cropBottomPixels=$(expr $curHeight / $cropBottom)
    fi
    newHeight=$(expr $curHeight - $cropBottomPixels - $cropTopPixels)

    # cropping the image

    convert $theInputFile -crop ${newWidth}x${newHeight}+${cropLeftPixels}+${cropTopPixels} $theOutputFile

done

