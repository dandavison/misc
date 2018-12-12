import operator
from collections import Counter
from functools import reduce
from math import sqrt

import numpy as np


def factorize(n):
    factorized = {}

    def _factorize(n):
        assert n > 0
        if n in factorized:
            return factorized[n]

        if n < 4:
            factors = Counter([n])
        else:
            for i in range(int(sqrt(n)), 2 - 1, -1):
                quot, rem = divmod(n, i)
                if not rem:
                    return factorize(i) + factorize(quot)
            else:
                factors = Counter([n])

        factorized[n] = factors
        return factors

    return _factorize(n)


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


SERIAL_NUMBER = 9445
SQUARE = get_array(SERIAL_NUMBER)
_CACHE = {}


def memoized(f):
    def inner(*args):
        if args not in _CACHE:
            _CACHE[args] = f(*args)
        return _CACHE[args]
    return inner


@memoized
def get_subsquare_sum(i, j, size):
    factorization = factorize(size)
    if len(factorization) == 1:
        return SQUARE[i:(i + size), j:(j + size)].sum()
    else:
        (largest_factor, largest_factor_exp), *others = sorted(factorization.items(), reverse=True)
        multiplicity = (largest_factor ** (largest_factor_exp - 1)
                        * reduce(operator.mul, (fac ** exp for fac, exp in others), 1))
        return sum(get_subsquare_sum(i + largest_factor * k,
                                     j + largest_factor * l,
                                     largest_factor)
                   for k in range(multiplicity)
                   for l in range(multiplicity))


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
                             for size in range(1, square_size)
                             for i in range(square_size - size + 1)
                             for j in range(square_size - size + 1))
    return max_coord
