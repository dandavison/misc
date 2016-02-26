#!/usr/bin/env python
from time import sleep
from select import select
import sys

from getch import getch
from twisted.internet.fdesc import setNonBlocking


setNonBlocking(sys.stdin.fileno())

while True:
    ready = select([sys.stdin], [], [], 0)[0]
    if ready:
        print [getch()]
    else:
        print '.'
        sleep(1)
