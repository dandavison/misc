#!/usr/bin/env python

def f():
    _a = 1

    class X(object):
        a = _a

    return X


print f()
