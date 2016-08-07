#!/usr/bin/env python
import os
import sys

# ls | tr a-z A-Z

# fork two children
# Child 1 runs 'ls'
# Child 2 runs 'tr a-z A-Z'

READ_END, WRITE_END = 0, 1

# It seems that it also works to defer pipe creation to the child1 process as
# below
pipe = os.pipe()

if os.fork() == 0:
    # In Child 1

    # pipe = os.pipe()

    if os.fork() > 0:
        # In Child 1
        # Send output to write end of pipe
        os.dup2(pipe[WRITE_END], sys.stdout.fileno())
        os.close(pipe[READ_END])
        os.execvp('ls', ['ls', '-al'])
    else:
        # In Child 2
        # Get input from read end of pipe
        os.close(pipe[WRITE_END])
        os.dup2(pipe[READ_END], sys.stdin.fileno())
        os.execvp('tr', ['tr', 'a-z', 'A-Z'])
else:
    # In parent python process; don't need to do anything
    pass
