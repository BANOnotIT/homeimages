# coding:utf-8

import glob
import os
import shutil
from datetime import datetime
from os.path import join, split, exists

import exifread
from tqdm import tqdm

from constants import (
    DATABASE_PHOTOS_PATH,
    POSSIBLE_STORAGE_PATHS,
    SYSTEM_PREPATH
)


def import_images(source_path):
    """ Find attached storage and run importing all existing images """
    print(source_path)

    globs = []
    for ext in ('jpg', 'jpeg', 'JPG', 'JPEG'):
        globs += glob.glob(join(source_path, '**', '*.' + ext))

    for path in tqdm(globs, 'coping', unit='image'):
        process_image(path)


def process_image(image_path):
    with open(image_path, 'rb') as f:
        try:
            created = str(exifread.process_file(f, 'Image DateTime')['Image DateTime'])
            d = datetime.strptime(created.split()[0], '%Y:%m:%d')
            targetpath = join(DATABASE_PHOTOS_PATH, '{:02}'.format(d.year), '{:02}'.format(d.month),
                              '{:02}'.format(d.day))
        except:
            targetpath = join(DATABASE_PHOTOS_PATH, 'UNTAGGED')

        target = join(targetpath, split(image_path)[1])

        if not exists(target):
            try:
                os.makedirs(targetpath)
            except:
                pass
            shutil.copyfile(image_path, target)


if __name__ == '__main__':

    source_path = None
    for each in POSSIBLE_STORAGE_PATHS:
        if exists(SYSTEM_PREPATH.format(each)):
            source_path = SYSTEM_PREPATH.format(each)
            break

    if not source_path:
        raise ValueError('Photos source path not found')

    import_images(source_path)
