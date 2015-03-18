    # extract all frames from the video file:
    ./frames-extractor.py 00017.MTS ~/tmp/frames/in
    
    # add the same camera exif data (focal length, camera make, camera model) to each frame
    ./add-exif-data.py ~/tmp/frames/in 2.8mm Panasonic HC-X900 1920 1080
    
    # make a new directory with links to a subset of all frames, for example, each 50th frame:
    ./frame-subsetter.py ~/tmp/frames/in ~/tmp/frames/out-49 49
