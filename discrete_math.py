#!/usr/bin/env python3
from collections import Counter
from copy import deepcopy
from itertools import product
from math import factorial as fac

from more_itertools import powerset


def choose(n, k):
    return fac(n) / (fac(k) * fac(n - k))


def classify_functions(domain_size, codomain_size):
    domain, codomain = set(range(domain_size)), set(range(codomain_size))
    relations = powerset(product(domain, codomain))

    def has_duplicates(_list):
        return len(set(_list)) == len(_list)

    def is_function(rel):
        _domain = [a for a, b in rel]
        return not has_duplicates(_domain)

    def is_injection(rel):
        image = [b for a, b in rel]
        return not has_duplicates(image)

    def is_surjection(rel):
        image = [b for a, b in rel]
        return set(image) == set(codomain)

    cnts = {
        'function': [],
        'injection': [],
        'surjection': [],
    }
    for rel in relations:
        print(rel)
        if is_function(rel):
            _domain = {a for a, b in rel}
            if _domain != domain:
                continue
            cnts['function'].append(rel)
            if is_injection(rel):
                cnts['injection'].append(rel)
            if is_surjection(rel):
                cnts['surjection'].append(rel)
    return cnts


def get_partitions(n):
    """
    Return a list of all partitions of the set {1, 2, ..., n}

    A partition is a list of parts.
    A part is a set.

    The parts of a partition are disjoint sets whose union is
    {1, 2, ..., n}
    """
    if n == 0:
        return [[]]
    else:
        partitions = []
        for partition in get_partitions(n - 1):

            # For each part of the n-1 partition, create a new
            # partition in which the new element is added to that part
            # and the other parts are unchanged.
            for i in range(len(partition)):
                _partition = deepcopy(partition)
                _partition[i].append(n)
                partitions.append(_partition)

            # Also create a new partition in which the new element is
            # added as a singleton.
            partitions.append(partition + [[n]])

        return partitions

def stirling_number_second_kind(n, k):
    """
    The number of partitions of size k of a set of size n.
    """
    return int((1/fac(k)) * sum(
        (-1)**i * choose(k, i) * (k - i)**n
        for i in range(k + 1)
    ))


def bell_number(n):
    """
    The number of partitions of a set of size n.
    """
    return sum(stirling_number_second_kind(n, k)
               for k in range(n + 1))
