#!/usr/bin/env python
import dateutil.parser
import yaml

print yaml.load("k: 2016-09-08T13:05:41.194099")  # datetime.datetime.now().isoformat()
# => {'k': datetime.datetime(2016, 9, 8, 13, 5, 41, 194099)}

print yaml.load("k: 2016-09-08")  # datetime.datetime.now().date().isoformat()
# => {'k': datetime.date(2016, 9, 8)}

print repr(dateutil.parser.parse("2016-09-08"))
# => datetime.datetime(2016, 9, 8, 0, 0)
