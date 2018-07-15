# coding:utf-8

import os
from os import path

from tqdm import tqdm

from settings import (DATABASE_PATH, CLOUD_PATH, KEY_FILE, ENCRYPTED_EXT)
from utils import get_files_in_dir_by_exts


def decrypt_files_to_home(source_path):
    """ Find attached storage and run importing all existing images """

    files = get_files_in_dir_by_exts(source_path, (ENCRYPTED_EXT,))

    for path in tqdm(files, 'decrypting', unit='file'):
        decrypt_file_and_move_to_home(path)


def decrypt_file_and_move_to_home(source_path):
    rel_path = path.relpath(source_path, CLOUD_PATH)

    target = path.join(DATABASE_PATH, rel_path).replace('.' + ENCRYPTED_EXT, '')

    target_dir = path.split(target)[0]

    if not path.exists(target):
        try:
            os.makedirs(target_dir)
        except:
            pass
        import subprocess

        CMD = 'openssl enc -aes-256-cbc -d -in "{}" -out "{}" -kfile "{}"'

        p = subprocess.Popen(CMD.format(source_path, target, KEY_FILE), shell=True)
        p.wait()


if __name__ == '__main__':
    decrypt_files_to_home(CLOUD_PATH)
