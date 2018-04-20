#!/usr/bin/env python3

from sympy import (
    Eq,
    cos,
    integrate,
    pi,
    plot,
    sin,
    solve,
    symbols,
    sqrt,
)
from sympy.plotting import plot_parametric

def make_symbols(*names):
    globals().update(zip(names, symbols(names)))


make_symbols('a', 'b', 'x', 'y', 't', 'theta')


eq = Eq(x, t * sp.exp(t))
solve(eq, t)
# [LambertW(x)]


plot_10_2_33 = plot_parametric(
    t**3 + 1,
    2*t - t**2,
)


# 10.2.34
A1 = integrate(-3 * a**2 * sin(theta)**4 * cos(theta)**2, (theta, pi/2, 0))

A2 = integrate(sqrt() (theta, 0, pi/2))


# Oxford M5 1.1.b
integrate(
    integrate(
        (x * y * cos(x**2 * y + y))
        (x, 0, b),
    ),
    (y, 0, a),
)
