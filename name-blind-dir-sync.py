import hashlib
import os

import dirtools


LEAF_DIRECTORY_EXTENSIONS = {'.epub', '.pdf'}


def sync_dirs(dir_1, dir_2):
    content_to_paths_1 = _get_content_to_paths(dir_1)
    content_to_paths_2 = _get_content_to_paths(dir_2)

    in_source_but_not_target = {
        path
        for key, path in content_to_paths_1.items()
        if key not in content_to_paths_2
    }

    for path in sorted(in_source_but_not_target):
        print 'cp ' + path + ' ' + dir_2


def _get_content_to_paths(dir_path):
    content = {}
    for _dir_path, dir_names, file_names in os.walk(dir_path):
        _process_and_remove_names(dir_names, _dir_path, content, _hash_directory)
        _process_and_remove_names(file_names, _dir_path, content, _hash_file)
    return content


def _process_and_remove_names(names, root_path, content, hash_function):
    for name in list(names):
        if any(name.endswith(ext)
               for ext in LEAF_DIRECTORY_EXTENSIONS):
            path = os.path.join(root_path, name)
            content[hash_function(path)] = path
            names.remove(name)


def _hash_directory(path):
    return dirtools.Dir(path).hash(dirtools.filehash)


def _hash_file(path):
    with open(path) as fp:
        return hashlib.md5(fp.read()).hexdigest()


if __name__ == '__main__':
    import sys
    sync_dirs(*sys.argv[1:])
