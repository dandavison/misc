#!/usr/bin/env python

import sys, bisect

v = [(0, 0)] # because of the "-1" at the end
for i in open(sys.argv[1]):
    a, b = i.split()
    v.append((int(a), 1))
    v.append((int(b), -1))
v.sort()

count = 0
for i in range(len(v)):
    count += v[i][-1]
    v[i] = (v[i][0], count)

# print v
# print sys.argv[2]

keys = [r[0] for r in v]

position = bisect.bisect(keys, int(sys.argv[2])) - 1
print v[position][-1] > 0
