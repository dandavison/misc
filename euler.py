from collections import Counter
from math import sqrt

from toolz import merge_sorted
from toolz import take


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


def eratosthenes():
    composite_sequences = []

    n = 2

    yield n

    # add the 2-sequence to the collection of sequences
    composite_sequences.append((2 * i for i in count(1)))

    while True:
        composites = merge_sorted(*composite_sequences)

        # yield the next number greater than n that is not composite
        n = next(
            i
            for i, j in enumerate(composites, n + 1)
            if i > n and i != j
        )
        yield n

        # add the new sequence of composites
        composite_sequences.append((n * i for i in count(1)))



def is_prime(n):
    return len(list(factorize(n).elements())) == 1
