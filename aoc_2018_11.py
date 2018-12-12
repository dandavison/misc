import operator
from collections import Counter
from functools import reduce
from math import sqrt

import numpy as np


def get_power_level(x, y, serial_number):
    """
    - Find the fuel cell's rack ID, which is its X coordinate plus 10.
    - Begin with a power level of the rack ID times the Y coordinate.
    - Increase the power level by the value of the grid serial number (your puzzle input).
    - Set the power level to itself multiplied by the rack ID.
    - Keep only the hundreds digit of the power level
      (so 12345 becomes 3; numbers with no hundreds digit become 0).
    - Subtract 5 from the power level.

    (3, 5)
    - The rack ID is 3 + 10 = 13.
    - The power level starts at 13 * 5 = 65.
    - Adding the serial number produces 65 + 8 = 73.
    - Multiplying by the rack ID produces 73 * 13 = 949.
    - The hundreds digit of 949 is 9.
    - Subtracting 5 produces 9 - 5 = 4
    """
    rack_id = x + 10
    power_level = rack_id * (rack_id * y + serial_number)
    power_level = (power_level % 1000) // 100
    power_level -= 5
    return power_level


def get_array(serial_number):
    array = np.zeros(shape=(300, 300))
    for i in range(300):
        for j in range(300):
            array[i, j] = get_power_level(i, j, serial_number)
    return array


def is_prime(n):
    for i in range(int(sqrt(n)), 2 - 1, -1):
        if n % i == 0:
            return False
    return True


SERIAL_NUMBER = 9445
SQUARE = get_array(SERIAL_NUMBER)
PRIMES = list(filter(is_prime, range(1, 300 + 1)))
_CACHE = {}


def memoized(f):
    def inner(*args):
        key = (f.__name__, args)
        if key not in _CACHE:
            _CACHE[key] = f(*args)
        return _CACHE[key]
    return inner


@memoized
def factorize(n):
    # Return (m, k) where m is the largest factor of n and m * k = n.
    for i in range(int(sqrt(n)), 2 - 1, -1):
        quot, rem = divmod(n, i)
        if not rem:
            return quot, n // quot
    return n, 1


@memoized
def largest_prime_factorize(n):
    # Return (m, k) where m is the largest prime factor of n and m*k = n.
    for i in reversed(PRIMES):
        quot, rem = divmod(n, i)
        if not rem:
            return i, quot


@memoized
def get_subsquare_sum(i, j, size):
    # fac1, fac2 = largest_prime_factorize(size)  This is even slower
    fac1, fac2 = factorize(size)
    if fac2 == 1:
        return SQUARE[i:(i + size), j:(j + size)].sum()
    else:
        return sum(get_subsquare_sum(i + fac1 * k, j + fac1 * l, fac1)
                   for k in range(fac2)
                   for l in range(fac2))


def get_max_subsquare_sum(size):
    [square_size] = set(SQUARE.shape)
    max_sum, max_coord = max((get_subsquare_sum(i, j, size), (i, j))
                             for i in range(square_size - size + 1)
                             for j in range(square_size - size + 1))
    return max_coord


def part1():
    return get_max_subsquare_sum(3)


def part2():
    [square_size] = set(SQUARE.shape)
    max_sum, max_coord = max((get_subsquare_sum(i, j, size), (i, j, size))
                             for size in range(square_size, 0, -1)
                             for i in range(square_size - size + 1)
                             for j in range(square_size - size + 1))
    return max_coord


print(part1())
print(part2())
