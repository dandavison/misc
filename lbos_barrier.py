"""
n threads should arrive at barrier. When the nth gets there, all proceed.
"""
from threading import Lock, Semaphore, Thread


n = 3
barrier = Semaphore(0)
mutex = Lock()
counter = 0


def make_thread(i: int):
    def closure():
        global counter
        print(f"{i}: rendezvous")
        mutex.acquire()
        counter += 1
        mutex.release()

        if counter == n:
            barrier.release()

        # "turnstile"
        barrier.acquire()
        barrier.release()

        print(f"{i}: critical section")

    return Thread(target=closure)


threads = [make_thread(i) for i in range(n)]


for t in threads:
    t.start()

for t in threads:
    t.join()
