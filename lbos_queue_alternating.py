"""
This works for n_leaders == n_followers but deadlocks otherwise
"""
from threading import Thread, Semaphore

leaders_queue = Semaphore(1)
followers_queue = Semaphore(0)


def make_leader_thread(i: int):
    def closure():
        leaders_queue.acquire()
        print(f"leader  {i} dance")
        followers_queue.release()

    return Thread(target=closure)


def make_follower_thread(i: int):
    def closure():
        followers_queue.acquire()
        print(f"follower {i} dance")
        leaders_queue.release()

    return Thread(target=closure)


n_leaders, n_followers = 3, 3
leaders = [make_leader_thread(i) for i in range(n_leaders)]
followers = [make_follower_thread(i) for i in range(n_followers)]

dancers = followers + leaders

for t in dancers:
    t.start()

for t in dancers:
    t.join()
