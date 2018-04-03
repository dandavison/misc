#!/usr/bin/env python3
import operator
from itertools import combinations
from functools import reduce

from toolz import compose


def P(n, k):
    return prod(n - i for i in range(0, k))


def C(n, k):
    return P(n, k) / P(k, k)


def prod(x):
    return reduce(operator.mul, x, 1)



def tucker_5_2_21():
    print('a')
    a_me = sum(
        C(4, m) * C(6, w)
        for m in [2, 3]
        for w in range(2 * m, 6 + 1)
    )
    a_tucker = C(4, 2) * (C(6, 4) + C(6, 5) + C(6, 6)) + C(4, 3) * C(6, 6)


    b_me = sum(
        C(9, n)
        for n in [3, 4, 5]
    )
    b_tucker = C(9, 3) + C(9, 4) + C(9, 5)


    c_me = C(10, 5) - C(7, 2)
    c_tucker = C(10, 5) - C(7, 2)

    print('a')
    print(a_me)
    print(a_tucker)
    print()

    print('b')
    print(b_me)
    print(b_tucker)
    print()

    print('c')
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
        men = {'m1', 'm2', 'm3', 'm4'}
        women = {'w1', 'w2', 'w3', 'w4'}

        return list(
            c
            for c in combinations(men | women, 4)
            if len(set(c) & women) >= 2
            and not {'m1', 'w1'} <= set(c)
        )

    def d_brute_2():
        """
        How many ways can a committee be formed from 4 men and 6 women with:
        4 members,
        >= 2 women,
        not including both Mr and Mrs Baggins?
        """
        men = {'m1', 'm2', 'm3', 'm4'}
        women = {'w1', 'w2', 'w3', 'w4'}
        people = list(men | women)

        ok = set()
        for i in range(0, len(people)):
            for j in range(i + 1, len(people)):
                for k in range(j + 1, len(people)):
                    for l in range(k + 1, len(people)):
                        c = people[i], people[j], people[k], people[l]
                        assert len(set(c)) == len(c)
                        if sum(p in women for p in c) >= 2:
                            if not ('m1' in c and 'w1' in c):
                                ok.add(c)
        return list(ok)

    d_me = (
        sum(
            C(4, m) * C(6, 4 - m)
            for m in [0, 1, 2, 3, 4]
        ) -
        sum(
            C(6, w) * C(4, 4 - w)
            for w in [2, 3, 4]
        ) -
        C(3, 2) * C(5, 0)
    )
    # Let the women be w1, w2, w3, wb
    # Let the men be m1, m2, m3, mb
    d_me_2 = (
        # Start with all sets of size 4
        C(10, 4)
        # Remove ones with 0 or 1 women (including one with wb and mb)
        - sum(
            C(6, w) * C(4, 4 - w)
            for w in [0, 1]
        )
        # Remove ones like {wb, w*, mb, m*}
        - C(5, 1) * C(3, 1)
        # Remove ones like {wb, w*, w*, mb}
        - C(5, 2)
    )
    d_tucker = (((C(4, 2) * C(6, 2)) - (3 * 5)) +
                ((C(4, 1) * C(6, 3)) - C(5, 2)) +
                C(6, 4))

    print('d')
    print(d_me)
    print('d_me_2: ', d_me_2)
    print('d_tucker: ', d_tucker)
    sort = compose(tuple, sorted)

    print('d_brute')
    cc = sort(map(sort, d_brute()))
    print(len(cc))
    print(len(set(cc)))
    # for c in cc:
    #     print(c)

    print('d_brute_2')
    cc = sort(map(sort, d_brute_2()))
    print(len(cc))
    print(len(set(cc)))
    # for c in cc:
    #     print(c)





def tucker_5_1_37():
    faces = [1, 2, 3, 4, 5, 6]
    rolls = lambda: ((i, j, k)
                for i in faces
                for j in faces
                for k in faces
                if min(i, j, k) == max(i, j, k) / 2)

    rolls_2 = [roll for roll in rolls()
               if len(set(roll)) == 2]

    rolls_3 = [roll for roll in rolls()
               if len(set(roll)) == 3]

    for roll in sorted(map(sorted, rolls_2)):
        print(sorted(roll))

    print()

    for roll in sorted(map(sorted, rolls_3)):
        print(sorted(roll))

    print()

    numer = len(rolls_2) + len(rolls_3)

    denom = 6**3
    print((numer, denom))


if __name__ == '__main__':
    tucker_5_2_21()
    # tucker_5_1_37()
