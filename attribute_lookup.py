#!/usr/bin/env python

# It seems that __getattr__ is called only after checking the other places
# (__dict__, methods, properties)

class X(object):

    def __init__(self):
        self.a = 1

    def __getattr__(self, name):
        raise Exception

    def m(self):
        return 'm'

    @property
    def p(self):
        return 'p'

    @staticmethod
    def sm():
        return 'sm'

    @classmethod
    def cm(cls):
        return 'cm'
