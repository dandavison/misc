import random
import time
from typing import List
from threading import Thread, Semaphore, Lock

data = -1

mutex = Semaphore(1)
room_empty = Semaphore(1)

n_readers = 0


def make_reader_thread(i: int):
    def closure():
        global n_readers
        with mutex:
            n_readers += 1
            if n_readers == 1:
                room_empty.acquire()

        print(f"reader {i}: read data: {data}")
        time.sleep(1)

        with mutex:
            n_readers -= 1
            if n_readers == 0:
                room_empty.release()

    return Thread(target=closure)


def make_writer_thread(i: int):
    def closure():
        global data
        room_empty.acquire()
        data = i
        print(f"writer {i}: data <- {data}")
        time.sleep(1)
        room_empty.release()

    return Thread(target=closure)


n_readers, n_writers = 15, 10
readers = [make_reader_thread(i) for i in range(n_readers)]
writers = [make_writer_thread(i) for i in range(n_writers)]

threads = writers + readers
random.shuffle(threads)

for t in threads:
    t.start()

for t in threads:
    t.join()
