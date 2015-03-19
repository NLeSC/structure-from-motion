#!/bin/sh

for i in IMG*.jpg
do
    echo convert $i -fuzz 15000 -fill white -opaque white -black-threshold 90% -blur 0x8 bla-$i
#    convert $i -fuzz 15000 -fill white -opaque white -black-threshold 90% -blur 0x8 bla-$i
done

cp black.png out.png

for i in bla-*.jpg
do
   echo composite -compose plus $i out.png out.png
   composite -compose plus $i out.png out.png
   echo convert out.png -fuzz 15000 -fill white -opaque white -black-threshold 25% out.png
   convert out.png -fuzz 15000 -fill white -opaque white -black-threshold 25% out.png
done





