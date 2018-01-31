#!/usr/bin/env python

from contextlib import contextmanager

if False:
    # Does not work; contextmanager may only yield once
    @contextmanager
    def retries(n):

        while n:
            try:
                yield
            except:
                print('In except')
                n -= 1
                if not n:
                    raise
            # finally:
            #     raise



    with retries(2):
        f()


def do_with_retries(f, n_retries):
    while n_retries:
        try:
            f()
        except:
            n_retries -= 1
            if not n_retries:
                raise

def f():
    print 'hello'
    raise Exception


do_with_retries(f, 3)
