#!/usr/bin/env python3
import operator
from itertools import combinations
from itertools import product
from functools import reduce

from toolz import compose


def P(n, k):
    """
    Number of k-tuples from a set of size n.
    """
    # P_multiset(n, (1,) * n)
    return prod(n - i for i in range(0, k))


def P_multiset(n, counts):
    """
    Number of n-tuples from a multiset.
    """
    assert sum(counts) == n
    return prod(C(n - sum(counts[:i]), counts[i]) for i in range(len(counts)))


def C(n, k):
    return int(P(n, k) / P(k, k))


def prod(x):
    return reduce(operator.mul, x, 1)


def permutations(x):
    """
    The permutations of [head] + tail are given by
    1. Find all permutations of tail
    2. For each tail permutation, and for each possible insertion position, emit a permutation with
       head inserted at that position.
    """
    x = tuple(x)
    if len(x) == 1:
        yield x
    else:
        head, *tail = x
        tail_perms = permutations(tail)
        for perm in tail_perms:
            for i in range(len(perm) + 1):
                yield perm[:i] + (head,) + perm[i:]


def interleavings(*lists):
    """
    Return all interleavings of lists.

    >>> interleavings()
    []

    >>> interleavings([1])
    [[1]]

    >>> interleavings([1], [2, 3])
    [[1, 2, 3], [2, 1, 3], [2, 3, 1]]

    >>> from math import factorial
    >>> choose = lambda n, k: (factorial(n) / factorial(n - k)) / factorial(k)
    >>> len(interleavings([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11])) == choose(11, 6)
    True
    >>> len(interleavings([1, 2, 3, 4], [5, 6, 7], [8, 9])) == choose(9, 4) * choose(5, 3)
    True
    """
    lists = [l for l in lists if l]
    if len(lists) == 1:
        return lists
    else:
        _interleavings = []
        for l in lists:
            head = l.pop(0)
            _interleavings.extend([head] + interleaving for interleaving in interleavings(*lists))
            l.insert(0, head)
    return _interleavings


def tests():
    assert P(10, 10) == P_multiset(10, (1,) * 10)


def tucker_5_2_21():
    print("a")
    a_me = sum(C(4, m) * C(6, w) for m in [2, 3] for w in range(2 * m, 6 + 1))
    a_tucker = C(4, 2) * (C(6, 4) + C(6, 5) + C(6, 6)) + C(4, 3) * C(6, 6)

    b_me = sum(C(9, n) for n in [3, 4, 5])
    b_tucker = C(9, 3) + C(9, 4) + C(9, 5)

    c_me = C(10, 5) - C(7, 2)
    c_tucker = C(10, 5) - C(7, 2)

    print("a")
    print(a_me)
    print(a_tucker)
    print()

    print("b")
    print(b_me)
    print(b_tucker)
    print()

    print("c")
    print(c_me)
    print(c_tucker)
    print()

    def d_brute():
        """
        How many ways can a committee be formed from 4 men and 6 women with:
        4 members,
        >= 2 women,
        not including both Mr and Mrs Baggins?
        """
        men = {"m1", "m2", "m3", "m4"}
        women = {"w1", "w2", "w3", "w4", "w5", "w6"}

        return list(
            c
            for c in combinations(men | women, 4)
            if len(set(c) & women) >= 2 and not {"m1", "w1"} <= set(c)
        )

    def d_brute_2():
        """
        How many ways can a committee be formed from 4 men and 6 women with:
        4 members,
        >= 2 women,
        not including both Mr and Mrs Baggins?
        """
        men = {"m1", "m2", "m3", "m4"}
        women = {"w1", "w2", "w3", "w4", "w5", "w6"}
        people = list(men | women)

        ok = set()
        for i in range(0, len(people)):
            for j in range(i + 1, len(people)):
                for k in range(j + 1, len(people)):
                    for l in range(k + 1, len(people)):
                        c = people[i], people[j], people[k], people[l]
                        assert len(set(c)) == len(c)
                        if sum(p in women for p in c) >= 2:
                            if not ("m1" in c and "w1" in c):
                                ok.add(c)
        return list(ok)

    d_me = (
        sum(C(4, m) * C(6, 4 - m) for m in [0, 1, 2, 3, 4])
        - sum(C(6, w) * C(4, 4 - w) for w in [2, 3, 4])
        - C(3, 2) * C(5, 0)
    )
    # Let the women be w1, w2, w3, wb
    # Let the men be m1, m2, m3, mb
    d_me_2 = (
        # Start with all sets of size 4
        C(10, 4)
        # Remove ones with 0 or 1 women (including one with wb and mb)
        - sum(C(6, w) * C(4, 4 - w) for w in [0, 1])
        # Remove ones like {wb, w*, mb, m*}
        - C(5, 1) * C(3, 1)
        # Remove ones like {wb, w*, w*, mb}
        - C(5, 2)
    )
    d_tucker = ((C(4, 2) * C(6, 2)) - (3 * 5)) + ((C(4, 1) * C(6, 3)) - C(5, 2)) + C(6, 4)

    print("d")
    print(d_me)
    print("d_me_2: ", d_me_2)
    print("d_tucker: ", d_tucker)
    sort = compose(tuple, sorted)

    print("d_brute")
    cc = sort(map(sort, d_brute()))
    print(len(cc))
    print(len(set(cc)))
    # for c in cc:
    #     print(c)

    print("d_brute_2")
    cc = sort(map(sort, d_brute_2()))
    print(len(cc))
    print(len(set(cc)))
    # for c in cc:
    #     print(c)


def tucker_5_1_37():
    faces = [1, 2, 3, 4, 5, 6]
    rolls = lambda: (
        (i, j, k) for i in faces for j in faces for k in faces if min(i, j, k) == max(i, j, k) / 2
    )

    rolls_2 = [roll for roll in rolls() if len(set(roll)) == 2]

    rolls_3 = [roll for roll in rolls() if len(set(roll)) == 3]

    for roll in sorted(map(sorted, rolls_2)):
        print(sorted(roll))

    print()

    for roll in sorted(map(sorted, rolls_3)):
        print(sorted(roll))

    print()

    numer = len(rolls_2) + len(rolls_3)

    denom = 6 ** 3
    print((numer, denom))


def tucker_5_3_ex_2():
    """
    How many different ways are there to select six hot dogs from three varieties of hot dog?
    """
    sort = compose(tuple, sorted)

    ans_1 = len(set(map(sort, product((1, 2, 3), repeat=6))))
    ans_2 = C(8, 6)
    assert ans_1 == ans_2
    return ans_1


def tucker_5_3_ex_5():
    """
    How many ways are there to form a sequence of 10 letters from four As, four Bs, four Cs, and
    four Ds if each letter must appear at least twice?
    """
    return P_multiset(4, (3, 1)) * P_multiset(10, (4, 2, 2, 2)) + P_multiset(
        4, (2, 2)
    ) * P_multiset(10, (3, 3, 2, 2))


def tucker_5_4_ex_4():
    """
    How many ways are there to distribute four identical oranges and six distinct apples (each a
    different variety) into five distinct boxes? In what fraction of these distributions does each
    box get exactly two objects?
    """
    denominator = (5 ** 6) * C(4 + 5 - 1, 5 - 1)
    numerator = (
        # Comments illustrate distributions of oranges in each case
        # {2, 2, 0, 0, 0}
        C(5, 2) * P_multiset(6, (2, 2, 2))
        +
        # {2, 1, 1, 0, 0}
        5 * C(4, 2) * 6 * 5 * P_multiset(4, (2, 2))
        +
        # {1, 1, 1, 1, 0}
        C(5, 4) * 6 * 5 * 4 * 3 * P_multiset(2, (2,))
    )
    return (numerator, denominator)


if __name__ == "__main__":
    tests()
