#!/bin/python3

import os
import sys

#
# Complete the climbingLeaderboard function below.
#
def getRank_3(score, scores):
    rank = 1
    cur = None
    for other_score in scores:
        if other_score <= score:
            break
        if other_score != cur:
            rank += 1
        cur = other_score
    # print("scores=%s, score=%d, rank=%d" % (scores, score, rank))
    return rank

def climbingLeaderboard_3(scores, alice):
    #
    # Write your code here.
    #
    return (getRank_3(score, scores) for score in alice)


from bisect import bisect_right as bisect

def getRank_2(score, scores):
    rank = 1
    cur = None
    for other_score in reversed(scores):
        if other_score <= score:
            break
        if other_score != cur:
            rank += 1
        cur = other_score
    # rank = len(scores) - rank - 1
    # print("scores=%s, score=%d, rank=%d" % (scores, score, rank))
    return rank


def climbingLeaderboard_2(scores, alice):
    #
    # Write your code here.
    #
    ranks = []
    prev_score = None
    scores.sort()
    for score in alice:
        if prev_score is not None:
            scores.remove(prev_score)
        scores.insert(bisect(scores, score), score)
        ranks.append(getRank_2(score, scores))
        prev_score = score
    return ranks


def getRank_1(score, scores):
    rank = 1
    cur = None
    for other_score in scores:
        if other_score <= score:
            break
        if other_score != cur:
            rank += 1
        cur = other_score
    # print("scores=%s, score=%d, rank=%d" % (scores, score, rank))
    return rank


def climbingLeaderboard_1(scores, alice):
    #
    # Write your code here.
    #
    ranks = []
    prev_score = None
    for score in alice:
        if prev_score is not None:
            scores.remove(prev_score)
        scores.append(score)
        scores.sort(reverse=True)
        ranks.append(getRank(score, scores))
        prev_score = score
    return ranks


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard_2(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
