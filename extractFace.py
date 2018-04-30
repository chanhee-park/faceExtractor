# Author : Chanhee
# Date : 2017.04.30
# What is the code to do :  Extract faces from all image files in 'directory' and save them in 'out_src'.

# - pip install ObjectExtractor ( OR pip3 install ObjectExtractor)

import os
from object_extractor import Extractor, FRONTALFACE_ALT2

CURRENT_PATH = os.path.dirname(__file__)
extensions = ['jpeg', 'png']

directory = './input'
out_src = './test'

index = 1

for dir_path, _, file_names in os.walk(directory):
    for filename in file_names:
        path = './' + os.path.relpath(os.path.join(dir_path, filename))
        if not filename.split('.')[-1] in extentions: continue
        print(path)
        Extractor.extract(os.path.join(CURRENT_PATH, path), cascade_file=FRONTALFACE_ALT2,
                          output_directory=os.path.join(CURRENT_PATH, out_src), output_prefix="face_" + str(index),
                          start_count=1)
        index = index + 1
