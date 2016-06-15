#!/usr/bin/env python
from mock import patch

__import__orig = __import__


def patched_import(name, *args, **kwargs):
    print name
    print
    for arg in args:
        print arg
    print
    for k, v in sorted(kwargs.items()):
        print k, v


    return __import__orig(name, *args, **kwargs)


with patch('__builtin__.__import__', side_effect=patched_import):
    from collections import namedtuple
