#!/usr/bin/env python
"""
Utility to check if a file's AST has changed versus master.

Usage:
python check.py file.py
"""
import ast
import os
import subprocess
import sys

if len(sys.argv) < 2:
    sys.stderr.write('you need to specify a file!\n')
    exit()

path = sys.argv[1]


def execute(cmd):
    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
    )
    output, error = process.communicate()
    if error:
        raise Exception
    return output

top_level = execute('git rev-parse --show-toplevel').rstrip()
cwd = os.getcwd()
assert cwd.find(top_level) == 0

full_path = os.path.join(
    cwd[len(top_level):].strip('/'),
    path
)

old_file = execute('git show master:%s' % full_path)

new_file = open(path).read()

if old_file == new_file:
    sys.stderr.write('the file has not been edited!\n')
    exit()

equivalent = ast.dump(ast.parse(old_file)) == ast.dump(ast.parse(new_file))

if equivalent:
    sys.stdout.write("The AST has remained the same (that's good)\n")
else:
    sys.stderr.write("The AST has changed (that's bad)\n")
    sys.exit(1)
