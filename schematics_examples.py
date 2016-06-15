#!/usr/bin/env python

from schematics.models import Model
from schematics.types.compound import DictType
from schematics.types.compound import ListType
from schematics.types import StringType


class Person(Model):
    name = StringType(required=True)


print Person({'name': 'dan'}).to_primitive()
