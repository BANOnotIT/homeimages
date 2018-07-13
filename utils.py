import glob
from os.path import join

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

from settings import DEFAULT_DIR_NAME


def fetch_metadata_from_file(filename):
    parser = createParser(filename)
    if not parser:
        return None

    with parser:
        try:
            metadata = extractMetadata(parser)
        except:
            return None

    return metadata


def get_path_from_metadata(metadata):
    if metadata is None:
        return DEFAULT_DIR_NAME

    date = metadata.get('creation_date', default=0)

    if date == 0:
        return DEFAULT_DIR_NAME
    else:
        return join('{:02}'.format(date.year), '{:02}'.format(date.month), '{:02}'.format(date.day))


def get_files_in_dir_by_exts(source_path, exts):
    globs = []
    for ext in exts:
        pattern = join(source_path, '**', '*.' + ext)
        globs += glob.glob(pattern, recursive=True)
    return globs
