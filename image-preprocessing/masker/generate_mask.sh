#!/bin/sh

for i in IMG*.jpg
do
    echo convert $i -channel Blue -separate -background black -combine +channel blue-$i
#    convert $i -channel Blue -separate -background black -combine +channel blue-$i
done

for i in blue-*.jpg
do
    echo convert $i -threshold 2% thres-$i
#    convert $i -threshold 2% thres-$i
done

#composite black.png black.png -blend 2 result.png

for i in thres-blue-*.jpg
do
    echo convert $i -blur 0x8 blur-$i
    convert $i -blur 0x8 blur-$i
done

cp black.png out.png

for i in blur-thres-blue-*.jpg
do
   echo composite -compose plus $i out.png out.png
   composite -compose plus $i out.png out.png
done


TODO

convert IMG_0034.jpg -fuzz 15000 -fill white -opaque white -black-threshold 90% -blur 0x8 bla.jpg




