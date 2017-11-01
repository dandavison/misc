#!/usr/bin/env python3
from collections import Counter
from collections import defaultdict
from copy import deepcopy
from itertools import product
from math import factorial as fac

from more_itertools import powerset


def choose(n, k):
    return fac(n) / (fac(k) * fac(n - k))


def classify_relations(A, B):
    def is_function(rel):
        domain = [a for a, b in rel]
        return len(set(domain)) == len(domain)

    def is_injection(rel):
        image = [b for a, b in rel]
        return len(set(image)) == len(image)


    def is_surjection(rel, codomain):
        image = [b for a, b in rel]
        return set(image) == set(codomain)

    A, B = range(A), range(B)
    relations = list(powerset(product(A, B)))

    cnts = defaultdict(list)
    for rel in relations:

        domain = [a for a, b in rel]
        if set(domain) != set(A):
            continue

        if is_function(rel):
            cnts['function'].append(rel)
            if is_injection(rel):
                cnts['injection'].append(rel)
            if is_surjection(rel, B):
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
