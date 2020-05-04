#!/bin/bash
# un-comment one diff tool you'd like to use

# side-by-side diff with custom options:
# sdiff -w200 -l "$2" "$5"
sdiff -w200 -l <(bat "$2") <(bat "$5")

# using kdiff3 as the side-by-side diff:
# kdiff3 "$2" "$5"

# using Meld
# meld "$2" "$5"

# using VIM
# vim -d "$2" "$5"
