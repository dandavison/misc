#!/usr/bin/env python

class Parent(object):
    def __init__(self):
        print 'Parent.__init__'

class MixinParent(object):
    def __init__(self):
        print 'MixinParent.__init__'
        super(MixinParent, self).__init__()

class Mixin(MixinParent):
    def __init__(self):
        print 'Mixin.__init__'
        super(Mixin, self).__init__()

class Child(Mixin, Parent):
    def __init__(self):
        super(Child, self).__init__()

print Child.mro()
