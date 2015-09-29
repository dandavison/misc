from contextlib import contextmanager
import os


@contextmanager
def open_for_writing(path):
    mode = get_mode(path)
    try:
        os.chmod(path, mode | 0o200)
        with open(path, 'w') as fp:
            yield fp
    finally:
        os.chmod(path, mode)


def get_mode(path):
    return int(oct(os.stat(path)[0] & 0o777), 8)
