#!/bin/bash -eu

file="$1"
mark="જઅ"
sed -i -e "/$mark/"'!'"s/^%PDF-\([0-9]\+\.[0-9]\+\)/%PDF-\1 $mark/" "$file"
