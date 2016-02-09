#!/usr/bin/env python3
from unittest import mock

from threading_mock_2_associated_module import Y
from threading_mock_2_associated_module import task_runner


def patching_method(self):
    print('patched method')

print('Unpatched')
task_runner.run_task_in_thread()

print()

print('Patched')
with mock.patch.object(Y, 'method_to_patch', patching_method):
    task_runner.run_task_in_thread()


# Output
# -----------------------------------------------------------------------------
# Unpatched
# unpatched method

# Patched
# patched method
# -----------------------------------------------------------------------------
