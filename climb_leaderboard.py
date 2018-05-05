#!/bin/python3

import os


def _merge_scores(x, y):
    if not x:
        return [(el, 2) for el in y]
    elif not y:
        return [(el, 1) for el in x]
    elif x[0] > y[0]:
        return [(x[0], 1)] + _merge_scores(x[1:], y)
    else:
        return [(y[0], 2)] + _merge_scores(x, y[1:])


def climbingLeaderboard(scores, alice):
    alice_ranks = {}
    OTHER, ALICE = 1, 2
    curr = scores[0]
    rank = 1

    for score, who in _merge_scores(scores, sorted(alice, reverse=True)):
        if who == OTHER and score < curr:
            rank += 1
            curr = score
        elif who == ALICE:
            alice_ranks[score] = rank if score >= curr else rank + 1

    return [alice_ranks[score] for score in alice]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
