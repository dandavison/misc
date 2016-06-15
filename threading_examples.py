from datetime import datetime
from threading import Thread
import time


def now():
    return datetime.now().isoformat(' ')


def task1():
    while True:
        print 'task1', now()
        time.sleep(1)


def task2():
    print 'task2', now()
    time.sleep(1)


thread1 = Thread(target=task1)
thread2 = Thread(target=task2)

thread1.start()
thread2.start()
