#!/usr/bin/env python3
import csv
from tempfile import NamedTemporaryFile

with NamedTemporaryFile(mode='w', delete=True) as f:
    w = csv.writer(f)
    w.writerow([b'a'])
