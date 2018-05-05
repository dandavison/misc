#!/bin/python3

import os
import sys


def _merge_scores(sorted_scores, unsorted_scores):
    sorted_scores_1 = iter(sorted_scores)
    sorted_scores_2 = iter(sorted(unsorted_scores, reverse=True))

    curr_1 = next(sorted_scores_1, None)
    curr_2 = next(sorted_scores_2, None)

    while True:
        if curr_1 is None:
            if curr_2 is not None:
                yield curr_2, 2
                yield from ((s, 2) for s in sorted_scores_2)
            break
        elif curr_2 is None:
            if curr_1 is not None:
                yield curr_1, 1
                yield from ((s, 2) for s in sorted_scores_1)
            break
        elif curr_1 > curr_2:
            yield curr_1, 1
            curr_1 = next(sorted_scores_1, None)
        elif curr_1 == curr_2:
            yield curr_1, 1
            yield curr_2, 2
            curr_1 = next(sorted_scores_1, None)
            curr_2 = next(sorted_scores_2, None)
        elif curr_2 > curr_1:
            yield curr_2, 2
            curr_2 = next(sorted_scores_2, None)


def climbingLeaderboard(scores, alice):
    alice_ranks = {}
    OTHER, ALICE = 1, 2
    curr = scores[0]
    rank = 1

    for score, who in _merge_scores(scores, alice):
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
