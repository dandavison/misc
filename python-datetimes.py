#!/usr/bin/env python
from datetime import datetime

import pytz


# This is just a timestamp, with no indication what timezone it is in. It
# doesn't contain any more information than the string '1-2-2017 00:00:00'.
# We do *not* know what point in time this is referring to.
naive_datetime = datetime.strptime('1-1-2017 00:00:00', '%m-%d-%Y %H:%M:%S')
print(repr(naive_datetime))
# datetime.datetime(2017, 1, 1, 0, 0)

# This is a python object which holds the raw timestamp, together with a
# specification that it is EST.
# We now know what point in time this is referring to.
aware_datetime = pytz.timezone('EST').localize(naive_datetime)
print(repr(aware_datetime))
# datetime.datetime(2017, 1, 1, 0, 0, tzinfo=<StaticTzInfo 'EST'>)

# Here is how to take a raw timestamp, interpret it as being in EST, and print
# out what a clock in London (UTC) would be displaying at that point in time:
naive_datetime = datetime.strptime('1-1-2017 00:00:00', '%m-%d-%Y %H:%M:%S')
EST = pytz.timezone('EST')
aware_datetime = EST.localize(naive_datetime)
print(aware_datetime.astimezone(pytz.timezone('UTC')))
# 2017-01-02 05:00:00+00:00

# One can construct timezones using an offset from GMT. Bizarrely however, the
# sign of the offset must be reversed from what one would expect. E.g. whereas
# EST is usually (IS0 8601) represented as GMT-5, one has to (POSIX) provide
# GMT+5 to pytz.
# https://stackoverflow.com/a/4009126/583763
# https://en.wikipedia.org/wiki/Tz_database
naive_datetime = datetime.strptime('1-1-2017 00:00:00', '%m-%d-%Y %H:%M:%S')
EST = pytz.timezone('Etc/GMT+5')
aware_datetime = EST.localize(naive_datetime)
print(aware_datetime.astimezone(pytz.timezone('UTC')))
# 2017-01-01 05:00:00+00:00
