#!/usr/bin/env python

class Parent(object):
    def __init__(self):
        print 'Parent.__init__'

class Mixin(object):
    def __init__(self):
        print 'Mixin.__init__'
        super(Mixin, self).__init__()

class Child1(Mixin, Parent):
    pass

class Child2(Mixin, Parent):
    def __init__(self):
        super(Child2, self).__init__()

Child1()
Child2()
