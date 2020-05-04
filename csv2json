#!/usr/bin/env python

import csv
import json
import sys


json.dump(
    list(csv.DictReader(sys.stdin, delimiter='\t', quotechar='"')),
    sys.stdout,
    indent=2,
)
