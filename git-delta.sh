#!/bin/bash

set -euo pipefail

git $@ | delta --24-bit-color always --theme GitHub --width variable --retain-plus-minus-markers --commit-style plain --file-style plain --hunk-style plain

exit_status=$?

echo $exit_status $0 $@ >> /tmp/git-delta.log

exit $exit_status
