#!/usr/bin/env python
import logging
import sys
from time import sleep
from multiprocessing.dummy import Pool as ThreadPool
import threading


A_THREAD_HAS_RAISED_AN_EXCEPTION = False


def say(s):
    sys.stdout.write(s + "\n")
    sys.stdout.flush()


def f(_):
    global A_THREAD_HAS_RAISED_AN_EXCEPTION
    thread_id = threading.current_thread().ident

    for i in range(3):
        say('hello from %d, i=%d' % (
            thread_id,
            i,
        ))
        sleep(1)
        if not A_THREAD_HAS_RAISED_AN_EXCEPTION:
            say('%d exiting' % thread_id)
            A_THREAD_HAS_RAISED_AN_EXCEPTION = True
            0/0

pool = ThreadPool(2)
pool.map(f, range(10))
pool.close()
pool.join()
