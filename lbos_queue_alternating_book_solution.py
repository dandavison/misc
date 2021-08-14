from threading import Thread, Semaphore

leaders_count = followers_count = 0
mutex = Semaphore(1)
leaders_queue = Semaphore(0)
followers_queue = Semaphore(0)
rendezvous = Semaphore(0)


def make_leader_thread(i: int):
    def closure():
        global followers_count
        global leaders_count
        mutex.acquire()
        if followers_count > 0:
            followers_count -= 1
            followers_queue.release()
        else:
            leaders_count += 1
            mutex.release()
            leaders_queue.acquire()

        print(f"leader  {i} dance")
        rendezvous.acquire()
        mutex.release()

    return Thread(target=closure)


def make_follower_thread(i: int):
    def closure():
        global followers_count
        global leaders_count
        mutex.acquire()
        if leaders_count > 0:
            leaders_count -= 1
            leaders_queue.release()
        else:
            followers_count += 1
            mutex.release()
            followers_queue.acquire()

        print(f"follower {i} dance")
        rendezvous.release()

    return Thread(target=closure)


n_leaders, n_followers = 3, 4
leaders = [make_leader_thread(i) for i in range(n_leaders)]
followers = [make_follower_thread(i) for i in range(n_followers)]

dancers = followers + leaders

for t in dancers:
    t.start()

for t in dancers:
    t.join()
