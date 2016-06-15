#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor


def task():
    print('In task')


with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(task)
    _ = future.result()
