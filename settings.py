# coding:utf-8


import os

from hachoir.core import config

# Turn off warnings on parsing
config.quiet = True

# Path on disk where all images and videos live
DATABASE_PHOTOS_PATH = os.path.expanduser('~/Изображения/SORTED/IMAGES')
DATABASE_VIDEOS_PATH = os.path.expanduser('~/Изображения/SORTED/VIDEOS')
DATABASE_PATH = os.path.expanduser('~/Изображения/SORTED')

# Directory name where SD usually is added
POSSIBLE_STORAGE_PATHS = ('Изображения/PHOTO', 'EOS_DIGITAL')

# system path to sd directories
SYSTEM_PREPATH = '/home/banonotit/{0}/'

CLOUD_PATH = '/home/banonotit/Mail.Cloud 1/Cloud Mail.Ru/Family_Lib'
KEY_FILE = './key-file'
ENCRYPTED_EXT = 'aes-256-cbc'

DEFAULT_DIR_NAME = 'UNTAGGED'
