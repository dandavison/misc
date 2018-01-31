#!/usr/bin/env python

from classproperty import classproperty

class X(object):
    x = 1

    @classproperty
    def x(cls):
        return 2


if __name__ == '__main__':
    print(X.x)
