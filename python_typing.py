from typing import Type, Union


class Bird:
    pass


class Mammal:
    pass


class Dog(Mammal):
    pass


dog: Union[Bird, Mammal] = Dog()

X = Union[str, int]

x: X = 1
y: X = "a"
z: X = {}
