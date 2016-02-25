#!/usr/bin/env python
from threading import Lock
from threading import Thread
from time import sleep

from getch import getch


class Reader(Thread):

    def __init__(self):
        super(Reader, self).__init__()
        self.buffer = []
        self.lock = Lock()

    def run(self):
        while True:
            self.lock.acquire()
            self.buffer.append(getch())
            self.lock.release()
            sleep(0)

    def read(self):
        self.start()
        while True:
            if self.buffer:
                # The reader may be in the middle of receiving multi-byte
                # input; wait long enough for this to finish.
                sleep(0.1)
                self.lock.acquire()
                chars, self.buffer = self.buffer, []
                self.lock.release()
                yield chars



if False:
    for chars in Reader().read():
        print chars


from select import select
from sys import stdin
import sys
import tty
import termios


def getch_non_blocking():
    ready = select([stdin], [], [], 0)[0]
    if ready:
        return ready[0].read(1)


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


if __name__ == '__main__':
    # for chars in read():
    #     print chars
    while True:
        char = getch_non_blocking()
        print [char]
        sleep(0.1)
