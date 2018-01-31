#!/bin/bash

set -u

command=$1; shift

tries=3

until $command "$@"; do
    (( --tries == 0 )) && exit 1
    echo $command "$@" failed, retrying...
    sleep 15
done
