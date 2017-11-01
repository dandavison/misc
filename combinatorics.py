#!/usr/bin/env python3

from math import factorial as fac

def choose(n, k):
    return fac(n) / (fac(k) * fac(n - k))


def n_injective_functions(n1, n2):
    """
    Number of injective functions from a set of size n1
    to a set of size n2.
    """
    def f(k):
        return choose(n1, k) * fac(n2) / fac(n2 - k)

    return sum(f(k) for k in range(min(n1, n2) + 1))


def n_surjective_functions(n1, n2):
    def f(k):
        return choose(n1, k) * fac(n1) * n1^(k - n1) / fac(k)

    return sum(f(k) for k in range(n1, n2 + 1))
