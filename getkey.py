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


def getch_non_blocking():
    if select([stdin], [], [])[0]:
        return getch()


def read():
    buf = []
    for char in getch_non_blocking():
        if char:
            buf.append(char)
        else:
            if buf:
                yield ''.join(buf)
                buf = []
            sleep(0.1)


if __name__ == '__main__':
    for chars in read():
        print chars
    # while True:
    #     char = getch_non_blocking()
    #     if char:
    #         print char
    #     else:
    #         sleep(0.1)
