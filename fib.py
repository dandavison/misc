#!/usr/bin/env python

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

    return map(ith, range(n))


print fib1(10)
print fib2(10)
print fib3(10)

