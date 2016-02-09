#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor


class X:
    def method_to_patch(self):
        print('unpatched method')


class Y(X):
    pass


def task():
    Y().method_to_patch()


class TaskRunner:
    def __init__(self, task):
        self.__task = task

    def run_task_in_thread(self):
        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(self.__task)
            _ = future.result()

task_runner = TaskRunner(task)
