import time
from typing import List
from threading import Thread, Semaphore, Lock

data = -1

rw_mutex = Semaphore(1)
readers_sem = Semaphore(0)

active_readers, blocked_readers = 0, 0
ar_mutex = Semaphore(1)


def make_reader_thread(i: int):
    def closure():
        with ar_mutex:
            if active_readers == 0:
                rw_mutex.acquire()
                readers_sem.release(blocked_readers)

            readers_sem.acquire()

            active_readers += 1

        print(f"reader {i}: read data: {data}")

        with ar_mutex:
            active_readers -= 1
            if active_readers == 0:
                rw_mutex.release()

    return Thread(target=closure)


def make_writer_thread(i: int):
    def closure():
        rw_mutex.acquire()
        global data
        data = i
        print(f"writer {i}: data <- {data}")
        rw_mutex.release()

    return Thread(target=closure)


n_readers, n_writers = 5, 3
readers = [make_reader_thread(i) for i in range(n_readers)]
writers = [make_writer_thread(i) for i in range(n_writers)]

threads = writers + readers

for t in threads:
    t.start()

for t in threads:
    t.join()
