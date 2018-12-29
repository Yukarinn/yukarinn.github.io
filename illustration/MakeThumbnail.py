#!usr/bin/python

import os, sys
from PIL import Image

IMAGE_FOLDER = "img"
THUMBNAIL_SIZE = 256, 256
THUMBNAIL_FOLDER = "thumbnail"

files = os.listdir(IMAGE_FOLDER)
for item in files:
    try:
        outFile = os.path.splitext(item)[0] + ".thumbnail"
        image = Image.open(os.path.join(IMAGE_FOLDER,item))
        image.thumbnail(THUMBNAIL_SIZE)
        image.save(os.path.join(THUMBNAIL_FOLDER, outFile), "JPEG")
    except IOError as e:
            print e
