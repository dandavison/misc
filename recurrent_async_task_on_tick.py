#!/usr/bin/env python
from time import sleep
from threading import Thread

import requests


TICKS = 0

def clock():
    global TICKS
    while True:
        sleep(0.5)
        TICKS += 1


def do_http_requests_forever():
    urls = ['https://www.theguardian.com'] * 3
    last_satisfied_tick = None

    while True:

        if TICKS == last_satisfied_tick:
            sleep(0.1)
            continue

        job_tick = TICKS
        responses = [requests.get(url) for url in urls]
        if TICKS == job_tick:
            print('%d %s' % (job_tick, [r.status_code for r in responses]))
            last_satisfied_tick = job_tick


clock_thread = Thread(target=clock)
clock_thread.start()

worker_thread = Thread(target=do_http_requests_forever)
worker_thread.start()
