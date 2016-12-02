#!/usr/bin/env python
from time import sleep
from multiprocessing.dummy import Pool as ThreadPool


def f():
    for i in range(3):
        print 'hello from f'
        sleep(1)


def g():
    for i in range(3):
        print 'hello from g'
        sleep(1)
        0/0

pool = ThreadPool(2)

pool.apply_async(f)
pool.apply_async(g)

pool.close()
pool.join()
