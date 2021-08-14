"""
Semaphores can also be used to represent a queue. In this case, the initial
value is 0, and usually the code is written so that it is not possible to signal
unless there is a thread waiting, so the value of the semaphore is never
positive.

For example, imagine that threads represent ballroom dancers and that two kinds
of dancers, leaders and followers, wait in two queues before entering the dance
floor.

When a leader arrives, it checks to see if there is a follower waiting. If so,
they can both proceed. Otherwise it waits.

Similarly, when a follower arrives, it checks for a leader and either proceeds
or waits, accordingly.

Puzzle: write code for leaders and followers that enforces these constraints.
"""
from threading import Thread, Semaphore

leader_queue = Semaphore(0)
follower_queue = Semaphore(0)


def make_leader_thread(i: int):
    def closure():
        print(f"leader   {i} waiting")
        follower_queue.release()
        leader_queue.acquire()
        print(f"leader   {i} dancing")

    return Thread(target=closure)


def make_follower_thread(i: int):
    def closure():
        print(f"follower {i} waiting")
        leader_queue.release()
        follower_queue.acquire()
        print(f"follower {i} dancing ***")

    return Thread(target=closure)


n_leaders = 3
n_followers = 3

followers = [make_follower_thread(i) for i in range(n_followers)]
leaders = [make_leader_thread(i) for i in range(n_leaders)]

dancers = followers + leaders

for t in dancers:
    t.start()

for t in dancers:
    t.join()
