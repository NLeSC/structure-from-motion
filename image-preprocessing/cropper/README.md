
Example usage:
```
./crop-image-sides.sh --in testimage --out cropped --cropSides 5 --cropTop 3
```
crops one fifth from the sides of the images in the 'testimage' directory, and one third from the top (nothing from the bottom).


'crop-image-sides.sh' crops all ``*.jpg|*.JPG`` (but not ``*.jpeg|*.JPEG``) in the ``--in`` directory. The amount of cropping is controlled by the ``--cropSides`` and ``--cropTop`` arguments. 

'crop-image-sides.sh' needs imagemagick's ``convert``. Install imagemagick using

```
sudo apt-get install imagemagick
```

