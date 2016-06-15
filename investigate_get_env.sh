#!/bin/bash

# | key exists? | default provided? | required? | behavior       |
# |-------------+-------------------+-----------+----------------|
# | yes         | -                 | -         | return value   |
# | no          | yes               | yes       | return default |
# | no          | yes               | no        | return default |
# | no          | no                | yes       | error          |
# | no          | no                | no        | return None    |


# | key exists? | default provided? | behavior       |
# |-------------+-------------------+----------------|
# | yes         | -                 | return value   |
# | no          | yes               | return default |
# | no          | no                | error          |


for val in True true TRUE 1 1L 1H None none for not ! == + { . 0. .0 .A +1 -1 int def @  b\'foo\' u\'foo\' u\'\' r\'foo\' જ += "<<" yield . .. : , ";" "1<<2" ; do
    echo "$val"
    echo -n "  " ; MYVAR="$val" python -c "from getenv import env; val = env('MYVAR') ; print val, type(val).__name__"
    echo -n "  "; MYVAR="$val" python -c "from get_env_var import get_env_var; val = get_env_var('MYVAR') ; print val, type(val).__name__"
    echo
done
