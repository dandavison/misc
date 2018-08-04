class ConditionVariable:

    def __init__(self):
        pass

    def wait(self, lock):
        # release the mutex (lock)
        # sleep until lock available
        # acquire on wake-up

    def signal(self):
        # tell one waiter that condition is now true


class Monitor:

    def __init__(self):
        self.lock = Lock()
        self.cond_var = ConditionVariable()




monitor = Monitor()

monitor.lock.acquire()
monitor.cond_var.signal()
