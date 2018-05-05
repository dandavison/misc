#!/usr/bin/env python

from math import sqrt

def fib1(n):
    last_two = (0, 1)
    vals = list(last_two)
    for i in range(max(n - 2, 0)):
        this = sum(last_two)
        vals.append(this)
        last_two = (last_two[1], this)

    return vals


def fib2(n):
    vals = [0, 1]
    for i in range(max(n - 2, 0)):
        vals.append(sum(vals[-2:]))
    return vals


def fib3(n):
    # memoize
    def ith(i):
        if i == 0:
            return 0
        elif i == 1:
            return 1
        else:
            return ith(i - 1) + ith(i - 2)

    return list(map(ith, range(n)))


def f(n):
    return (1/sqrt(5)) * (((1 + sqrt(5))/2)**n + ((1 - sqrt(5))/2)**n)

fib = fib2


def generating_function(x, n):
    # For numerical debugging of symbolic algebra.  A generating function should be thought of as a
    # formal power series really, not a function.
    return sum(
        a_i * x**i
        for a_i, i in zip(fib(n), range(n))
    )


def generating_function_2(x):
    return 1 / (1 - x - x**2)


def generating_function_3(x):
    return 4 / (
        (2*x - 1 - sqrt(5)) * (2*x - 1 + sqrt(5))
    )


def generating_function_4(x):
    return ((1 / sqrt(5)) *
            ((1 / (2*x - 1 - sqrt(5))) +
             (1 / (2*x - 1 + sqrt(5)))))


if __name__ == '__main__':
    print()
    print(fib1(10))
    print(fib2(10))
    print(fib3(10))
