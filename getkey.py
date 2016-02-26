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
