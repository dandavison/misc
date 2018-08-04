#!/usr/bin/env python3

class X:
    def __hash__(self):
        return 1

class Y:
    def __hash__(self):
        return 1

print({hash(X()): 'x',
       hash(Y()): 'y'})
