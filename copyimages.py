# coding:utf-8

import os
from os.path import join, exists, split

from tqdm import tqdm

from settings import (POSSIBLE_STORAGE_PATHS, SYSTEM_PREPATH, DATABASE_PHOTOS_PATH)
from utils import get_path_from_metadata, fetch_metadata_from_file, get_files_in_dir_by_exts


def import_images(source_path):
    """ Find attached storage and run importing all existing images """

    files = get_files_in_dir_by_exts(source_path, ('jpg', 'jpeg', 'JPG', 'JPEG'))

    for path in tqdm(files, 'processing', unit='image'):
        process_image(path)


def process_image(image_path):
    metadata = fetch_metadata_from_file(image_path)
    target_dir = join(DATABASE_PHOTOS_PATH, get_path_from_metadata(metadata))

    target = os.path.join(target_dir, split(image_path)[1])

    if not exists(target):
        try:
            os.makedirs(target_dir)
        except:
            pass
        import shutil
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
