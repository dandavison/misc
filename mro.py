#!/usr/bin/env python

class Parent(object):
    def __init__(self):
        print 'Parent.__init__'

class Mixin(object):
    def __init__(self):
        print 'Mixin.__init__'
        super(Mixin, self).__init__()

class Child(Mixin, Parent):
    def __init__(self):
        super(Child, self).__init__()

print Child.mro()
