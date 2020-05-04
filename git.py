import sys
from sys import argv
from subprocess import run, PIPE

sys.path = [p for p in sys.path if p]

git_cmd = ["git"] + argv[1:]

with open("/tmp/gitlog.log", "a") as f:
    f.write(" ".join(git_cmd) + "\n")

run(git_cmd, stdin=PIPE, stdout=PIPE)
