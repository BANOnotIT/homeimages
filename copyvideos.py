# coding:utf-8

import glob
import os
import subprocess
from os.path import join, exists, split

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from tqdm import tqdm

from constants import (
    POSSIBLE_STORAGE_PATHS,
    SYSTEM_PREPATH,
    DATABASE_VIDEOS_PATH
)


def metadata_for_filelike(filename):
    parser = createParser(filename)
    if not parser:
        return None

    with parser:
        try:
            metadata = extractMetadata(parser)
        except:
            return None

    return metadata


CMD = 'ffmpeg -loglevel panic -i "{}" -vcodec h264 -acodec aac -strict -2 "{}"'


def import_videos(source_path):
    """ Find attached storage and run importing all existing images """
    print(source_path)

    globs = []
    for ext in ('mov', 'MOV'):
        globs += glob.glob(join(source_path, '**', '*.' + ext))

    for path in tqdm(globs, 'processing', unit='video'):
        process_video(path)


def process_video(video_path):
    metadata = metadata_for_filelike(video_path)
    if metadata:
        d = metadata.get('creation_date')
        targetpath = join(DATABASE_VIDEOS_PATH, '{:02}'.format(d.year), '{:02}'.format(d.month),
                          '{:02}'.format(d.day))
    else:
        targetpath = join(DATABASE_VIDEOS_PATH, 'UNTAGGED')

    target = os.path.join(targetpath, split(video_path)[1].lower().replace('.mov', '.mp4'))

    if not os.path.exists(target):
        try:
            os.makedirs(targetpath)
        except:
            pass

        # print(CMD.format(video_path, target))

        p = subprocess.Popen(CMD.format(video_path, target), shell=True)
        p.wait()


if __name__ == '__main__':

    source_path = None
    for each in POSSIBLE_STORAGE_PATHS:
        if exists(SYSTEM_PREPATH.format(each)):
            source_path = SYSTEM_PREPATH.format(each)
            break

    if not source_path:
        raise ValueError('Photos source path not found')

    import_videos(source_path)
