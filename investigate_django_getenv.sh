#!/bin/bash

for val in True true TRUE 1 1L 1H None none for not ! == + { . 0. .0 .A +1 int def @  b\'foo\' u\'foo\' r\'foo\'; do
    echo -n "$val => "
    MYVAR="$val" python -c "from getenv import env; val = env('MYVAR') ; print val, type(val).__name__"
done
