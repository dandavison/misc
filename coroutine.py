#!/usr/bin/env python3

def coro():
    print('line 1')
    yield 'val1'
    val = (yield)
    print('got %r' % val)
    yield 'val2'
    print('line 2')


def gen():
    print('line 1')
    yield 'val1'
    print('line 2')
    yield 'val2'
    print('line 3')


c = coro()
c.send
