#!/bin/bash
GIT=/PATH/TO/REAL/git
start_ms=$(date '+%s%3N')
$GIT "$@"
status=$?
end_ms=$(date '+%s%3N')
ms=$((end_ms - start_ms))
cmd="$(basename $0) $*"
echo "${ms}ms: $cmd" >>/tmp/git.log
exit $status
