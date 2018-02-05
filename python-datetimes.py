#!/usr/bin/env python
from datetime import datetime

import pytz


# This is just a timestamp, with no indication what timezone it is in.
# It doesn't contain any more information than the string '1-2-2017 00:00:00'
naive_datetime = datetime.strptime('1-2-2017 00:00:00', '%m-%d-%Y %H:%M:%S')
# >>> naive_datetime
# >>> datetime.datetime(2017, 1, 2, 0, 0)

# This is a python object which holds the raw timestamp, together with a
# specification that it is EST
aware_datetime = pytz.timezone('EST').localize(naive_datetime)
# >>> aware_datetime
# >>> datetime.datetime(2017, 1, 2, 0, 0, tzinfo=<StaticTzInfo 'EST'>)

# Here is how to take a raw timestamp, interpret it as being in EST, and print
# out what the corresponding timestamp is in UTC:
naive_datetime = datetime.strptime('1-2-2017 00:00:00', '%m-%d-%Y %H:%M:%S')
aware_datetime = pytz.timezone('EST').localize(naive_datetime)
print(aware_datetime.astimezone(pytz.timezone('UTC')))
# 2017-01-02 05:00:00+00:00
