from functools import partial


def f(a, b):
    print a, b

fp = partial(f, 'partial_arg')

