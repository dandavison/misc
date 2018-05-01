#!/usr/bin/env python
from time import sleep
from threading import Thread


TICKS = 0

def clock():
    global TICKS
    while True:
        sleep(1)
        TICKS += 1


def report():
    while True:
        sleep(1)
        print(TICKS)


clock_thread = Thread(target=clock)
clock_thread.start()

reporter_thread = Thread(target=report)
reporter_thread.start()
