#!/usr/bin/env python
import sys
import subprocess
import xmltodict
import yaml

input = open(sys.argv[1]) if sys.argv[1:] else sys.stdin
bat = subprocess.Popen(["bat", "--plain", "--language", "yaml"], stdin=subprocess.PIPE)
yaml.dump(xmltodict.parse(input.read(), dict_constructor=dict), stream=bat.stdin, encoding="utf-8")
bat.communicate()
