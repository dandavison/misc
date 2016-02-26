#!/usr/bin/env python
from time import sleep
from select import select
import sys
import tty
import termios


def setNonBlocking(fd):
    """
    Set the file description of the given file descriptor to non-blocking.

    Copied from twisted source: twisted.internet.fdesc.setNonBlocking
    """
    flags = fcntl.fcntl(fd, fcntl.F_GETFL)
    flags = flags | os.O_NONBLOCK
    fcntl.fcntl(fd, fcntl.F_SETFL, flags)




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
