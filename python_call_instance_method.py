#!/usr/bin/env python

class X:
    def m(self):
        return 'm'



class Y:

    f = staticmethod(lambda x: x + 1)

    def __init__(self):
        print(self.f(1))


Y()
