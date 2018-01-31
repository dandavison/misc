#!/usr/bin/env python3
from itertools import chain

def get_paths_1(x):
    if not x:
        return [[]]
    paths = []
    for path in get_paths(x[1:]):
        paths.append()
        paths.append([x[0][1]] + path)

    return paths


def get_paths(x):
    if not x:
        return [[]]
    return chain.from_iterable(
        ([x[0][0]] + path,
         [x[0][1]] + path)
        for path in get_paths(x[1:]))


def get_path_sums(x):
    if not x:
        return [0]
    return chain.from_iterable(
        (x[0][0] + path_sum,
         x[0][1] + path_sum)
        for path_sum in get_path_sums(x[1:]))


x = [
    (0, 1),
    (2, 3),
    (4, 5),
    (6, 7),
]

for path in get_path_sums(x):
    print(path)
