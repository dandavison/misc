#!/usr/bin/env python
import subprocess
import sys
import time


for char in sys.stdin.read():
    subprocess.check_call(["osascript", "-e", f'tell application "Emacs" to keystroke "{char}"'])
    time.sleep(0.05)
