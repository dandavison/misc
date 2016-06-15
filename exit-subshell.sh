#!/bin/bash

die () {
    echo "$@" >&2
    exit 1
}

f () {
    die "exiting!"
}

a=$(f) ; echo hello
