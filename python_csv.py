#!/usr/bin/env python3
import csv
from io import BytesIO

w = csv.writer(BytesIO())
w.writerow(['a'])

# TypeError: a bytes-like object is required, not 'str'
# Because the default delimiter is unicode, I believe.
