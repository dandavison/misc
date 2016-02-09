#!/usr/bin/env python3
from threading_mock_2_associated_module_2 import TaskRunner


class X:
    def method_to_patch(self):
        print('unpatched method')


class Y(X):
    pass


def task():
    Y().method_to_patch()


task_runner = TaskRunner(task)
