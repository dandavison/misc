#!/usr/bin/env python
from time import sleep
from select import select
import sys
import tty
import termios

from twisted.internet.fdesc import setNonBlocking


fd = sys.stdin.fileno()
setNonBlocking(fd)
old = termios.tcgetattr(fd)

try:
    tty.setraw(fd)
    while True:
        ready = select([fd], [], [], 0)[0]
        if ready:
            print [sys.stdin.read(1)]
        else:
            print '.'
            sleep(1)
finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old)
