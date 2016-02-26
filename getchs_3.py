#!/usr/bin/env python
from time import sleep
from select import select
import fcntl
import os
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


def getchs():
    """
    Block until there are bytes to read on stdin and then return them all.

    Adapted from getch() in https://github.com/joeyespo/py-getch.
    """
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    setNonBlocking(fd)
    try:
        tty.setraw(fd)
        while not select([fd], [], [], 0)[0]:
            sleep(0.1)
        return sys.stdin.read()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


if __name__ == '__main__':
    while True:
        print '%r' % getchs()
