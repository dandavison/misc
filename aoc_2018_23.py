import numpy as np
import re
import sys


def parse_line(line):
    data = re.match('pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)', line).groups()
    return [int(n) for n in data]


def get_data(fp):
    data = np.array([parse_line(line) for line in fp])
    return data[:, :3], data[:, 3]


def n_in_range(x, r, i):
    strength, strongest = r[i], x[i]
    distances = np.abs(x - strongest).sum(axis=1)
    return (distances <= strength).sum()


def part1(x, r):
    return n_in_range(x, r, r.argmax())


with open('input') as fp:
    x, r = get_data(fp)

print(part1(x, r))
