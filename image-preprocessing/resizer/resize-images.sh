#!/bin/bash


exampleUsageStr='~/patty/data$ ../resizer/resize-images.sh --in ./SITES_image_based/SITE_662/ --out ./SITES_image_based_resized/SITE_662'

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


mkdir -p $theOutputDir


files=$(find $theInputDir -maxdepth 1 -type f -iname '*.jpg')

for f in $files; do

    echo "Processing file: $f..."
    fileName=${f##*/}

    theInputFile=$theInputDir/$fileName
    theOutputFile=$theOutputDir/$fileName

    # resizing the image
    # (the smallest dimension will be 500 pixels long after conversion)
    convert $theInputFile -resize 500x500^  $theOutputFile

done

