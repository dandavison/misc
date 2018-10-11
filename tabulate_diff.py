#!/usr/bin/env python
from __future__ import print_function
import sys

from collections import Counter

from clint.textui import colored


green = lambda s: colored.green(s, bold=True, always=True)
red = lambda s: colored.red(s, bold=True, always=True)

empty_change = lambda: ['', '']

changes = []
change = empty_change()

for line in sys.stdin:
    if line.startswith('-'):
        change[0] += line
    elif line.startswith('+'):
        change[1] += line
    else:
        if any(change):
            changes.append(tuple(change))
            change = empty_change()

changes = Counter(changes)

for change, count in changes.most_common():
    print(count)
    print(red(change[0]), end='')
    print(green(change[1]), end='')
    print()


