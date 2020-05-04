# 1. At import, construct
#    1. a map file_path ==> module_namespace
# 2. At reload
#    1. For every modified file:
#       1. Import the file
#       2. For every object defined in the file
#          1. For every module namespace referencing that object, replace the reference


from mock import patch

__import__orig = __import__


def patched_import(name, *args, **kwargs):
    print(name)
    print('\nargs')
    for arg in args:
        print(arg)
    print('\nkwargs')
    for k, v in sorted(kwargs.items()):
        print(k, v)
    print('------------------------------------')

    return __import__orig(name, *args, **kwargs)


with patch('builtins.__import__', side_effect=patched_import):
    from collections import namedtuple
