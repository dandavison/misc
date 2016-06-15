#!/usr/bin/env python
from threading import Thread
from time import sleep

from getch import getch


var = 1


class Thread1(Thread):
    def run(self):
        while True:
            print var
            sleep(1)


class Thread2(Thread):
    def run(self):
        print 'thread 2'
        while True:
            pass


Thread1().start()
Thread2().start()
