#!/usr/bin/env python

from contextlib import contextmanager


@contextmanager
def context_manager_test(arg):
    print 'before: %s' % arg
    try:
        yield
    finally:
        print 'after'


with context_manager_test('my_argument'):
    print 'hello'
    raise Exception
