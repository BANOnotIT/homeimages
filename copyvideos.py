# coding:utf-8

import os
from os.path import join, exists, split

from tqdm import tqdm

from settings import (POSSIBLE_STORAGE_PATHS, SYSTEM_PREPATH, DATABASE_VIDEOS_PATH)
from utils import get_path_from_metadata, fetch_metadata_from_file, get_files_in_dir_by_exts


def import_videos(source_path):
    """ Find attached storage and run importing all existing images """

    files = get_files_in_dir_by_exts(source_path, ('mov', 'MOV', 'avi', 'AVI', 'mp4', 'MP4'))

    for path in tqdm(files, 'processing', unit='video'):
        process_video(path)


def process_video(video_path):
    metadata = fetch_metadata_from_file(video_path)
    target_dir = join(DATABASE_VIDEOS_PATH, get_path_from_metadata(metadata))

    target = os.path.join(target_dir, split(video_path)[1])

    from os.path import splitext
    target = splitext(target)[0] + '.mp4'

    if not exists(target):
        try:
            os.makedirs(target_dir)
        except:
            pass
        import subprocess

        CMD = 'ffmpeg -loglevel panic -i "{}" -vcodec h264 -acodec aac -strict -2 "{}"'

        p = subprocess.Popen(CMD.format(video_path, target), shell=True)
        p.wait()


if __name__ == '__main__':

    source_path = None
    for each in POSSIBLE_STORAGE_PATHS:
        if exists(SYSTEM_PREPATH.format(each)):
            source_path = SYSTEM_PREPATH.format(each)
            break

    if not source_path:
        raise ValueError('Videos source path not found')

    import_videos(source_path)
