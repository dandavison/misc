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

    # turn back to string to do substition
    if False:
        # This does get rid of the braces, but quotes: '$placeholder'
        string_data = yaml.dump(python_data, default_style='block')
    else:
        # This uses braces: {key2: $placeholder}
        string_data = yaml.dump(python_data, default_flow_style=False)

    dt = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')

    print('Intermediate string before substitution')
    print(string_data)

    string_data = string.Template(string_data).substitute(placeholder=dt)

    print('Intermediate string after substitution')
    print(string_data)

    # Must be yaml.load
    python_data = yaml.load(string_data)  # read back to dict  ! bug

    print('Final python object')

    return python_data  # need datetime objects


def g():
    yaml_data = \
    """
    key1:
      {a: 99}
    key2:
      {
        a: 2018-10-05T17:29:12Z
      }
    """
    return yaml.load(yaml_data)



def h():
    datetime_obj = datetime.datetime.now()


print(f())
