#!/usr/bin/env python
from functools import partial


class X(object):

    def __init__(self, arg):
        self.arg = arg


constructor = partial(X, arg=9)

print(constructor().__dict__)
