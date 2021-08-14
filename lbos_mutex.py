import time
from threading import Semaphore, Thread

count = 0

lock = Semaphore(1)


def thread_A():
    global count
    lock.acquire()
    count = count + 1
    lock.release()


def thread_B():
    global count
    lock.acquire()
    count = count + 1
    lock.release()


t1 = Thread(target=thread_A)
t2 = Thread(target=thread_B)

t1.start()
t2.start()

t1.join()
t2.join()
print(count)
