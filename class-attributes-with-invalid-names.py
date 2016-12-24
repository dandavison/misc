#!/usr/bin/env python

class X(object):
    a = 1
    locals().update({'a[0]': 2})


class X(object):
    a = 1
    b = a + 1
