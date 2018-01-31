#!/usr/bin/env python3


class Base(object):
    def m(self):
        d = {'Base': 'Base'}
        return d


class Mixin1(object):
    def m(self):
        d = super(Mixin1, self).m()
        d['Mixin1'] = 'Mixin1'
        return d


class Mixin2(object):
    def m(self):
        d = super(Mixin2, self).m()
        d['Mixin2'] = 'Mixin2'
        return d


class X(Mixin1, Mixin2, Base):
    pass


print(X().m())
