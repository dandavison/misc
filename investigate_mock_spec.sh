#!/bin/bash

for val in True true TRUE 1 1L 1H ; do
    echo -n "$val => "
    MYVAR=$val python -c "from getenv import env; val = env('MYVAR') ; print val, type(val)"
done
