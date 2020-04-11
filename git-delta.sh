#!/bin/bash

echo "$@" >> /tmp/git-delta.log

set -o pipefail

DELTA=~/.facet/facets/magit-delta/delta

if $(grep -qE "( show | diff )" <<< "$@"); then
    git "$@" | $DELTA \
                   --24-bit-color always \
                   --theme GitHub \
                   --max-line-distance=0.6 \
                   --tabs 0 \
                   --width variable \
                   --retain-plus-minus-markers \
                   --commit-style plain \
                   --file-style plain \
                   --hunk-style plain
else
    git "$@"
fi
