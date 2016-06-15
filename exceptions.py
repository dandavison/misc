import sys

import six

def f():
    raise KeyError()

try:
    f()
except Exception as exc:
    exc_cls, inst, tb = sys.exc_info()
    import ipdb ; ipdb.set_trace()
    six.reraise(type(exc), exc, tb)
