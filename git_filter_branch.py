#!/usr/bin/env python
import datetime
import os
import sys
from textwrap import dedent


def main(commit, minutes_ago):
    commit_time = datetime.datetime.now() - datetime.timedelta(minutes=minutes_ago)
    os.system(dedent(f"""\
    git filter-branch --force --env-filter \
        'if [ $GIT_COMMIT = {commit} ]
         then
             export GIT_AUTHOR_DATE="{commit_time.isoformat()}"
             export GIT_COMMITTER_DATE="{commit_time.isoformat()}"
         fi' -- {commit}~1...HEAD\
    """))


if __name__ == '__main__':
    [commit, minutes_ago] = sys.argv[1:]
    assert len(commit) == 40
    minutes_ago = int(minutes_ago)
    main(commit, minutes_ago)
