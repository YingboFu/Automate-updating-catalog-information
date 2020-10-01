#!/usr/bin/env python3

import os
from PIL import Image

# TODO: change the path to match the experimental environment
path = 'supplier-data/images'

for filename in os.listdir(path):
    if filename.endswith('.tiff'):
        im = Image.open(os.path.join(path, filename))
        im.convert("RGB").resize((600, 400)).save(os.path.join(path, filename.replace('.tiff', '.jpeg')))
