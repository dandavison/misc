# See pipe-1.py
# Child 1 runs 'ls'
# Child 2 runs 'tr a-z A-Z'
import sys
from subprocess import Popen
from subprocess import PIPE

child_2 = Popen(["tr", "a-z", "A-Z"], stdin=PIPE, stdout=sys.stdout)
child_1 = Popen(["ls"], stdin=sys.stdin, stdout=child_2.stdin)
child_2.communicate()
