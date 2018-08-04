#!/usr/bin/env python

from attr import attrib
from attr import attrs


@attrs
class X(object):
    _a = attrib()
