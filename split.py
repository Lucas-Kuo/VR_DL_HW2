import os
from random import shuffle
import shutil

CUR_BASE_DIR = "train/train/"
VAL_BASE_DIR = "train/valid/"

files = []

for i in range(33402):
    files.append(str(i+1))

shuffle(files)

for filename in files[:3000]:
    print("Working with {}".format(filename))
    cur_img = CUR_BASE_DIR + filename + ".png"
    cur_txt = CUR_BASE_DIR + filename + ".txt"

    dest_img = VAL_BASE_DIR + filename + ".png"
    dest_txt = VAL_BASE_DIR + filename + ".txt"

    shutil.move(cur_img, dest_img)
    shutil.move(cur_txt, dest_txt)
