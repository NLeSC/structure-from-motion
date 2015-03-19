
Usage example:
```
./resize-images.sh --in ./testimage --out resized
```


'resize-images.sh' resizes all ``*.jpg|*.JPG`` (but not ``*.jpeg|*.JPEG`` ) in the ``--in`` directory , such that the smallest dimension will be 500 pixels long after conversion. The output is written in the ``--out`` directroy, which is created if it doesn't already exist.

'resize-images.sh' needs imagemagick's ``convert``. Install imagemagick using:

```
sudo apt-get install imagemagick
```
