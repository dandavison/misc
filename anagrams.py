#!/usr/bin/env python
import sys
from collections import defaultdict, Counter

anagrams = defaultdict(list)
for line in sys.stdin:
    word = line.strip()
    key = ''.join(sorted(word))
    anagrams[key].append(word)

for key in sorted(anagrams):
    words = anagrams[key]
    if len(words) > 1:
        sys.stdout.write('\n'.join(anagrams[key]) + '\n\n')
