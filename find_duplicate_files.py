#!/usr/bin/env python3

from collections import defaultdict
from hashlib import md5


def find_duplicates(file_paths):
    duplicates = []
    hash2path = {}
    for path in file_paths:
        with open(path) as fp:
            hash = md5(fp.read().encode('utf-8')).hexdigest()
        if hash in hash2path:
            duplicates.append((hash2path[hash], path))
        else:
            hash2path[hash] = path
    return duplicates


if __name__ == '__main__':
    import sys
    file_paths = [line.strip() for line in sys.stdin]
    print(find_duplicates(file_paths))
