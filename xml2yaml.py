#!/usr/bin/env python
import sys
import subprocess
from collections import OrderedDict
import xmltodict
import yaml

def ordered_dict_representer(dumper, data):
    return dumper.represent_mapping(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, data.items())

yaml.Dumper.add_representer(OrderedDict, ordered_dict_representer)
input = open(sys.argv[1]) if sys.argv[1:] else sys.stdin
bat = subprocess.Popen(["bat", "--plain", "--language", "yaml"], stdin=subprocess.PIPE)
yaml.dump(xmltodict.parse(input.read()), stream=bat.stdin, encoding="utf-8")
bat.communicate()
