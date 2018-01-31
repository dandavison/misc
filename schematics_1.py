#!/usr/bin/env python
from schematics.models import Model
from schematics.types import StringType

class Bird(Model):
    genus = StringType()
    species = StringType()


bird = Bird({
    'genus': 'Merops',
    'species': 'apiaster',
})
print(bird.__dict__)
