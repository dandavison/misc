#!/usr/bin/env python

from schematics.models import Model
from schematics.types import FloatType
from schematics.types import IntType
from schematics.types import StringType
from schematics.types.compound import DictType
from schematics.types.compound import ListType
from schematics.types.compound import ModelType


class Person(Model):
    name = StringType(required=True)


print Person({'name': 'dan'}).to_primitive()




class Wing(Model):
    length = FloatType()
    wing_bars = IntType()


class Bird(Model):
    length = FloatType()
    wing = ModelType(Wing)


bird = Bird({
    'length': 13.5,
    'wing': {
        'length': 7.88,
        'wing_bars': 2,
    }
})


if __name__ == '__main__':
    print(bird)
