#!/usr/bin/env python

class X(object):

    def __init__(self):
        self._a = 0

    @property
    def a(self):
        return self._a

class Y(X):
    # @property
    # def a(self):
    #     return self._a

    @a.setter
    def a(self, val):
        self._a = val


x = X()
print x.a
y = Y()
print y.a
y.a = 1
print y.a
