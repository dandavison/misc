from typing import List
from threading import Thread, Semaphore, Lock

queue: List[str] = list()
mutex = Lock()
queue_sem = Semaphore(0)


def make_producer_thread(i: int):
    def closure():
        with mutex:
            # TODO: block until buffer has space

            # Do we need to enqueue and increment semaphore atomically?
            queue.insert(0, f"task from producer {i}")
            print(f"producer {i} enqueued task")
        queue_sem.release()

    return Thread(target=closure)


def make_consumer_thread(i: int):
    def closure():
        while True:
            queue_sem.acquire()  # block if queue is empty
            with mutex:
                task = queue.pop()
            print(f"consumer {i} dequeued task: {task}")

    return Thread(target=closure)


n_producers, n_consumers = 17, 3
producers = [make_producer_thread(i) for i in range(n_producers)]
consumers = [make_consumer_thread(i) for i in range(n_consumers)]

threads = consumers + producers

for t in threads:
    t.start()

for t in threads:
    t.join()
