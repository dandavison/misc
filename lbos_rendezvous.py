import time
from threading import Semaphore, Thread

a_arrived = Semaphore(0)
b_arrived = Semaphore(0)


def thread_A():
    print("a1")
    a_arrived.release()
    b_arrived.acquire()
    print("a2")


def thread_B():
    print("b1")
    b_arrived.release()
    a_arrived.acquire()
    print("b2")


t1 = Thread(target=thread_A)
t2 = Thread(target=thread_B)

print("should be: {a1, b1} < {a2, b2}")
t1.start()
t2.start()

t1.join()
t2.join()
