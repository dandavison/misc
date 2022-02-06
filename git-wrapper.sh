#!/bin/bash
start_ms=$(date '+%s%3N')
cmd="$(basename $0) $@"
if [ "$cmd" = "git status -z -u" ]; then
    cmd="$cmd (=> git status -z)"
    /opt/twitter_mde/bin/git status -z
else
    /opt/twitter_mde/bin/git "$@"
fi
status=$?
end_ms=$(date '+%s%3N')
ms=$((end_ms - start_ms))
echo "${ms}ms: $cmd" >>/tmp/git-input
exit $status
