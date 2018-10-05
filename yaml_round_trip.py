#!/usr/bin/env python
from __future__ import print_function

import datetime
import json
import string

import yaml


def f(json=False):
    yaml_data = \
    """
    key1: 2018-10-05T17:01:31Z
    key2: $placeholder
    """

    print('Initial YAML string')
    print(yaml_data)

    python_data = yaml.load(yaml_data)

    print('Parsed python object')
    print(python_data)

    if json:
        string_data = json.dumps(python_data)
    else:
        string_data = yaml.dump(python_data)

    dt = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')

    string_data = string.Template(string_data).substitute(placeholder=dt)

    print('Intermediate string')
    print(string_data)

    if json:
        python_data = json.loads(string_data)
    else:
        python_data = yaml.load(string_data)

    print('Final python object')

    return python_data


print(f())
