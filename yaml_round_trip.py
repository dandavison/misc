#!/usr/bin/env python
from __future__ import print_function

import datetime
import json
import string

import yaml


def f():
    yaml_data = \
    """
    key2: $placeholder
    """

    print('Initial YAML string')
    print(yaml_data)

    python_data = yaml.load(yaml_data)  # python dict

    print('Parsed python object')
    print(python_data)

    string_data = yaml.dump(python_data)  # turn back to string to do substition

    dt = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')

    string_data = string.Template(string_data).substitute(placeholder=dt)

    print('Intermediate string')
    print(string_data)

    python_data = yaml.load(string_data)  # read back to dict  ! bug

    print('Final python object')

    return python_data


print(f())
