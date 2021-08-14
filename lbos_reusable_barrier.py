"""
Often a set of cooperating threads will perform a series of steps in a loop and
synchronize at a barrier after each step. For this application we need a
reusable barrier that locks itself after all the threads have passed through.

Puzzle: Rewrite the barrier solution so that after all the threads have passed
through, the turnstile is locked again.
"""
from threading import Thread, Semaphore, Lock

turnstile = Semaphore(0)
mutex = Lock()
count = 0


def make_thread(i):
    def closure():
        global count
        print(f"{i}: rendezvous")
        mutex.acquire()
        count += 1
        mutex.release()

        if count == n:
            turnstile.release()

        # turnstile
        turnstile.acquire()

        mutex.acquire()
        count -= 1
        if count > 0:
            turnstile.release()
        mutex.release()

        print(f"{i}: critical section")

    return Thread(target=closure)


n = 3
threads = [make_thread(i) for i in range(n)]

for t in threads:
    t.start()

for t in threads:
    t.join()

# # check turnstile is locked
# turnstile.acquire()
# print("error: expected deadlock")
