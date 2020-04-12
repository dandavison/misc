#!/bin/bash

echo "$@" >> /tmp/git-delta.log

set -o pipefail

if $(grep -qE "( show | diff )" <<< "$@"); then
    git "$@" | delta \
                   --color-only \
                   --24-bit-color always \
                   --theme GitHub \
                   --max-line-distance=0.6
else
    git "$@"
fi
