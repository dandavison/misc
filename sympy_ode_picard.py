#!/usr/bin/env python3

from sympy import (
    integrate,
    symbols,
)

t, y, tau = symbols('t y tau')


def picard(f, y_prev, a, b):
    """
    Return next picard iterate.

    y_next(t) = b + \int_a^\tau f(\tau, y) d\tau
    """
    return b + integrate(f.subs([(t, tau), (y, y_prev)]), (tau, a, t))


a, b = 0, 1

y = b
for i in [1, 2, 3]:
    f = (1 - 2*t) * y
    y_next = picard(f, y, a, b)
    print(y_next)
    y = y_next
