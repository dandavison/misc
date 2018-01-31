#!/usr/bin/env python
from contextlib import contextmanager


@contextmanager
def assertRaisesIf(exception, condition):
    if condition:
        with self.assertRaises(exception):
            yield
    else:
        yield


with assertRaisesIf(Exception, True):
    raise Exception
