#!/usr/bin/env python

from scipy.optimize import bisect


def record_optimization(func):

    def recorder(self, *args):
        if not hasattr(self, '_recorder_inputs'):
            self._recorder_inputs = []
        if not hasattr(self, '_recorder_outputs'):
            self._recorder_outputs = []

        self._recorder_inputs.append(args)
        output = func(self, *args)
        self._recorder_outputs.append(output)
        return output

    return recorder


class Optimizer():
    def __init__(self):
        self.target = 5.

    def optimize(self):
        print 'finding target...\nerror:',
        solution = bisect(self.error_function, -100, 100, xtol=0.1)
        print '\nsolution:', solution

    @record_optimization
    def error_function(self, x):
        print x - self.target,
        return x - self.target


optimizer = Optimizer()
optimizer.optimize()
print optimizer._recorder_inputs
print optimizer._recorder_outputs
