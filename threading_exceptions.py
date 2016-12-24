#!/usr/bin/env python
from time import sleep

from threading import Thread


class Worker1(Thread):

    def run(self):
        while True:
            print('In thread 1')
            sleep(1)
            raise ValueError



class Worker2(Thread):

    def run(self):
        while True:
            print('In thread 2')
            sleep(5)
            # raise ValueError

print('In main thread (1)')

worker2 = Worker2()
worker2.run()
worker2.join(1)

print('In main thread (2)')


worker1 = Worker1()
worker1.run()
#worker1.join(1)




print('In main thread (3)')

sleep(999999)
