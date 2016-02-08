#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from unittest import mock


class X:
    def method_to_patch(self):
        print('unpatched method')


def patching_method(self):
    print('patched method')


class Y(X):
    pass


def task():
    Y().method_to_patch()


print('Main thread')
with mock.patch.object(Y, 'method_to_patch', patching_method):
    task()
print()

print('`threading`')
with mock.patch.object(Y, 'method_to_patch', patching_method):
    thread = Thread(target=task)
    thread.start()
    thread.join()
print()

print('`concurrent.futures`')
with mock.patch.object(Y, 'method_to_patch', patching_method):
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(task)
        _ = future.result()

# Output:
# -----------------------------------------------------------------------------
# Main thread
# patched method

# `threading`
# patched method

# `concurrent.futures`
# patched method
# -----------------------------------------------------------------------------
