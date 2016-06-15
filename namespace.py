#!/usr/bin/env python

class X(object):

    def floating():
        return 'floating'

    print floating()

    def method(self):
        print 'method ' + floating()


X().method()
