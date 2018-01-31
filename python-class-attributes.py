#!/usr/bin/env python

class X(object):
    a = 1
    b = a + 1


class Y(X):
    a = Y.b


print Y().a
