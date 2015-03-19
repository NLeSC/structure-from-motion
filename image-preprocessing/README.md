
In some cases, it can be advantageous to preprocess the images. The repository includes scripts to:
* [crop](cropper)  the edges;
* [calculate](masker) a mask;
* [resize](resizer) image to make them more managable.

Both these rely on imagemagick for the heavy lifting. Imagemgick can be installed with:

```
sudo apt-get install imagemagick
```

