from copy import deepcopy

class X(object):
    def __init__(self, a):
        self.aa = [a]

x1 = X(1)
x1.b = [2]
x2 = deepcopy(x1)


clone(x1)

def clone(obj):
    new_data = deepcopy(obj.__dict__)

    new_obj = object()
    type(new_obj) = type(obj)
    new_obj.__dict__ = obj.__dict__
    return new_obj



def f(iterable):
    sentinel = object()
    iterable.append(sentinel)

    for item in iterable:
        # do something
        if item == sentinel:
            # terminate
