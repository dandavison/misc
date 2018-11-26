#!/usr/bin/env python

import csv
import sys

reader = csv.reader(sys.stdin)
writer = csv.writer(sys.stdout, delimiter="\t")
for row in reader:
    writer.writerow(row)
