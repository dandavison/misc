#!/usr/bin/env python
from contextlib import contextmanager
from unittest import TestCase


class Test(TestCase):

    @contextmanager
    def assertRaisesIf(self, exception, condition):
        if condition:
            with self.assertRaises(exception):
                yield
        else:
            yield

    def test(self):
        with self.assertRaisesIf(Exception, True):
            with self.noop():
                raise Exception

        with self.assertRaisesIf(Exception, False):
            with self.noop():
                raise Exception

    @contextmanager
    def noop(self):
        yield

