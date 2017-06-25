from collections import OrderedDict
from itertools import product

import pandas as pd


def possible_parents_of_2_positive_child():
    return (possible_parents_of_1_plus_1_minus_child() |
            possible_parents_of_2_plus_0_child())


def possible_parents_of_1_plus_1_minus_child():
    _1_plus_parents = [
        # (1, 1),  Impossible if SNP alt never occurs with 1-copy allele
        (2, 1),
        (3, 1),
    ]
    _1_minus_parents = [
        (1, 0),
        (2, 0),
        (2, 1),
        (3, 0),
        (3, 1),
    ]
    return set(product(_1_plus_parents, _1_minus_parents))


def possible_parents_of_2_plus_0_child():
    _2_plus_parents = [
        (2, 1),
        (3, 1),
    ]
    _0_parents = [
        (1, 0),
        # (1, 1),  Impossible if SNP alt never occurs with 1-copy allele
        (2, 0),
        (2, 1),
    ]
    return set(product(_2_plus_parents, _0_parents))


def all_likelihood_surfaces():
    P_snp_given_cn = list(product([0 * i for i in range(1, 10)],
                                  [0 * i for i in range(1, 10)],
                                  [0 * i for i in range(1, 10)]))

    surfaces = None
    for parents in sorted(possible_parents_of_2_positive_child()):
        print(parents)
        trio = 'key'
        try:
            surface = pd.DataFrame({trio: [0] * len(P_snp_given_cn)}, index=P_snp_given_cn)
        except Exception as ex:
            print("%s: %s" % (ex.__class__.__name__, ex))
            raise
        else:
            if surfaces is None:
                surfaces = surface
            else:
                surfaces = surfaces.join(surface)
    return surfaces


if __name__ == '__main__':
    all_likelihood_surfaces()
