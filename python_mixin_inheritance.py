#!/usr/bin/env python3

class Base(object):
    def m(self):
        d = {'Base': 'Base'}
        return d


class Mixin1(object):
    def m(self):
        return super(Mixin1, self).m()


class Mixin2(object):
    def m(self):
        return super(Mixin2, self).m()


class X(Mixin1, Base):
    pass


print(X().m())
