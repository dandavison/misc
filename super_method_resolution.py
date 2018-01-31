#!/usr/bin/env python

class Parent(object):

    def __init__(self):
        self.method()

    def method(self):
        print 'Parent.method'


class Child(Parent):

    def __init__(self):
        super(Child, self).__init__()

    def method(self):
        print 'Child.method'


####################################################

class Parent1(object):

    def __init__(self):
        self.method()

    def method(self):
        print 'Parent1.method'


class Parent2(object):

    def __init__(self):
        self.method()

    def method(self):
        print 'Parent1.method'


class Child(Parent1, Parent2):

    def __init__(self):
        super(Child, self).__init__()

    def method(self):
        print 'Child.method (before super)'
        super(Child, self).method()
        print 'Child.method (after super)'


Child()
