#!/usr/bin/env python

fallbacks = {
    'c': 'cval',
}


class X(object):
    """
    x = X()
    x.a => aval
    x.b => bval
    x.c => cval
    """

    def __init__(self):
        self.a = 'aval'
        # __dict__

    @property
    def b(self):
        return 'bval'

    def __getattr__(self, name):
        return fallbacks.get(name)


if __name__ == '__main__':
    import sys
    name, = sys.argv[1:]
    x = X()
    print getattr(x, name)  # x.xxx
    print vars(x)
