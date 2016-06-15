#!/usr/bin/env python3
from time import sleep

import threading


class Thread(threading.Thread):
    def run(self):
        sleep(999999)


thread = Thread(daemon=True)
thread.start()
