from collections import Counter
from collections import defaultdict
from itertools import product

from more_itertools import powerset


def is_function(rel):
    domain = [a for a, b in rel]
    return len(set(domain)) == len(domain)


def is_injection(rel):
    image = [b for a, b in rel]
    return len(set(image)) == len(image)


def is_surjection(rel, codomain):
    image = [b for a, b in rel]
    return set(image) == set(codomain)


def classify_relations(A, B):
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
