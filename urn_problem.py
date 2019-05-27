import sys

import numpy as np
from functools import lru_cache
from numpy import random

memoized = lru_cache(maxsize=None)

BLACK, WHITE = 1, 2

sys.setrecursionlimit(10000)

@memoized
def P_last_is_black(b, w, prev=None):
    """
    Note: the rules are flipped in this function! You stop when you encounter the first one of the
    other color. It gives 50% always.

    Calculate probability that last removed ball is black.

    b:    number of black balls
    w:    number of white balls
    prev: color of previously removed ball
    """
    if b == 0:
        return 0.0
    elif w == 0:
        return 1.0
    else:
        # Probability conditional on removing black next
        if prev == WHITE:
            P_last_is_black_given_remove_black = P_last_is_black(b,     w, None)
        else:
            P_last_is_black_given_remove_black = P_last_is_black(b - 1, w, BLACK)

        # Probability conditional on removing white next
        if prev == BLACK:
            P_last_is_black_given_remove_white = P_last_is_black(b,     w, None)
        else:
            P_last_is_black_given_remove_white = P_last_is_black(b, w - 1, WHITE)

        P_remove_black = b / (b + w)
        P_remove_white = 1 - P_remove_black

        return (P_remove_black * P_last_is_black_given_remove_black +
                P_remove_white * P_last_is_black_given_remove_white)


def last_color(b, w):
    """
    An urn contains n1 black and n2 white balls. You remove balls from the urn in a sequence of
    ``sessions''. In a single session you randomly remove one ball at a time until the first
    consecutive pair of same-colored balls is encountered. When this occurs, the second ball of the
    pair is replaced, and you start a new session. What is the color of the last remaining ball?
    """
    n = {BLACK: b, WHITE: w}
    prev = None
    while n[BLACK] + n[WHITE] > 1:
        curr = BLACK if random.uniform() <= n[BLACK] / (n[BLACK] + n[WHITE]) else WHITE
        if curr != prev:
            n[curr] -= 1
            prev = curr
        else:
            prev = None
    return BLACK if n[BLACK] else WHITE


def estimate_prob_last_is_black(b, w, N):
    """
    Return estimated probability of color 1 being last.
    """
    return sum(last_color(b, w) == BLACK for _ in range(N)) / N


if __name__ == '__main__':
    n, N = map(int, sys.argv[1:])
    for b in range(n + 1):
        # p = estimate_prob_last_is_black(b, n - b, N)
        p2 = P_last_is_black(b, n - b)
        p3 = P_last_is_black(100 * b, 100 * (n - b))
        print(f'{b:2d}  {p2:.3f}  {p3:.3f}')
        # print(f'{b:2d}  {p:.3f}  {p2:.3f}')
        # print(f'{b:2d}  {p:.3f}  {1/p if p else np.inf:.3f} {p2:.3f}')
