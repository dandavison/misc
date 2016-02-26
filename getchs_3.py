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
    Return all bytes available for reading on stdin, or None if there are none.

    Adapted from getch() in https://github.com/joeyespo/py-getch.
    """
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    setNonBlocking(fd)
    try:
        tty.setraw(fd)
        data = ''
        while True:
            while select([fd], [], [], 0)[0]:
                data += sys.stdin.read()
            if data:
                return data
            sleep(0.1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


if __name__ == '__main__':
    from time import sleep

    while True:
        print '%r' % getchs()
        sleep(0.5)
