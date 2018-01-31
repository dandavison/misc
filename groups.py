from sympy import Set


class Group(object):

    def __init__(self, set, operation):
        self.set = set
        self.operation = operation

    def is_subgroup(self, other):
        return (self.operation == other.operation,
                self.set <= other.set)
