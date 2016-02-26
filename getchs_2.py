#!/usr/bin/env python
from select import select
from sys import stdin
from time import sleep
import sys
import tty
import termios


def getch_non_blocking_2():
    fd = stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        if select([stdin], [], [], 0)[0]:
            char = stdin.read(1)
            return char
        else:
            return None
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def read():
    buf = []
    while True:
        char = getch_non_blocking()
        print [char]
        if char is not None:
            buf.append(char)
        else:
            if buf:
                yield buf
                buf = []
            sleep(0.1)


import fcntl
import os
def setNonBlocking(fd):
    """
    Set the file description of the given file descriptor to non-blocking.
    """
    flags = fcntl.fcntl(fd, fcntl.F_GETFL)
    flags = flags | os.O_NONBLOCK
    fcntl.fcntl(fd, fcntl.F_SETFL, flags)


def getch_non_blocking():
    setNonBlocking(stdin.fileno())

    ready = select([stdin], [], [], 0)[0]
    if ready:
        return ready[0].read(1)


if __name__ == '__main__':
    while True:
        char = getch_non_blocking()
        print [char]
        sleep(0.1)
