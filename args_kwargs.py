#!/usr/bin/env python

class X(object):
    def f(self, model, exclude_validation=None, **kwargs):
        print model, exclude_validation, kwargs


X().f(1, 2, exclude_validation=3)
