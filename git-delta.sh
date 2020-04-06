#!/bin/bash

if $(grep -qE "( show | diff )" <<< "$@"); then
    handler=delta
    set -o pipefail
    git $@ | delta --24-bit-color always --theme GitHub --width variable --retain-plus-minus-markers --commit-style plain --file-style plain --hunk-style plain
else
    handler=git
    git $@
fi

exit_status=$?

echo $exit_status $handler $@ >> /tmp/git-delta.log

exit $exit_status
