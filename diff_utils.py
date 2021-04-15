import json
import os

from difflib import unified_diff
from subprocess import Popen, PIPE


def print_source(source, language="go"):
    """
    https://github.com/sharkdp/bat/
    """
    proc = Popen(["bat", "--language", language], stdin=PIPE)
    proc.stdin.write(source.encode("utf-8"))  # type: ignore
    proc.communicate()


def to_json(obj):
    return json.dumps(obj, sort_keys=True, indent=2)


def print_diff(a, b, formatter=to_json):
    """
    https://github.com/dandavison/delta
    """
    if not (isinstance(a, str) and isinstance(b, str)):
        a = formatter(a)
        b = formatter(b)
    diff = "\n".join(unified_diff(a.splitlines(), b.splitlines()))
    if not diff:
        print("✅")
    else:
        os.environ["BAT_PAGER"] = "cat"
        proc = Popen(["delta"], stdin=PIPE)
        proc.stdin.write(diff.encode("utf-8"))  # type: ignore
        proc.communicate()
