#!/bin/bash
set -o pipefail

if $(grep -qE "( show | diff )" <<< "$@"); then
    git "$@" | delta --24-bit-color always \
                     --theme GitHub \
                     --width variable \
                     --retain-plus-minus-markers \
                     --commit-style plain \
                     --file-style plain \
                     --hunk-style plain \
                     --max-line-distance=0.6
else
    git "$@"
fi

exit_status=$?

echo "$@" >> /tmp/git-delta.log

exit $exit_status
