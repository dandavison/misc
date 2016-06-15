#!/bin/bash

f() {
    local x=9
    g
}


g() {
    echo "__${x}__"
}

f
