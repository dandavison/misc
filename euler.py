from collections import Counter
from math import sqrt


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
