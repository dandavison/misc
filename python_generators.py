#!/usr/bin/env python2

def gen(arg):
    if arg == 'abort':
        # I want to stop the stream here. Maybe I just encountered an error.
        return
    yield arg
