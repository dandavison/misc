import sys
from collections import Counter

from numpy import random


def last_type(n1, n2):
    """
    An urn contains n1 black and n2 white balls. You remove balls from the urn in a sequence of
    ``sessions''. In a single session you randomly remove one ball at a time until the first
    consecutive pair of same-colored balls is encountered. When this occurs, the second ball of the
    pair is replaced, and you start a new session. What is the color of the last remaining ball?
    """
    n = {1: n1, 2: n2}
    last_color = None
    while n[1] + n[2] > 1:
        next_color = 1 if random.uniform() <= n[1] / (n[1] + n[2]) else 2
        if next_color != last_color:
            n[next_color] -= 1
            last_color = next_color
        else:
            last_color = None
    return 1 if n[1] else 2



def frequency(x):
    counts = Counter(x)
    total = sum(counts.values())
    return {k: n / total for k, n in counts.most_common()}



if __name__ == '__main__':
    n1, n2, N = map(int, sys.argv[1:])
    print(frequency(last_type(n1, n2) for _ in range(N)))
