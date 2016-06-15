FOO=""
[ -z "$FOO" ]; echo $?
[ -n "$FOO" ]; echo $?
[[ -z $BAR ]]; echo $?
[[ -n $BAR ]]; echo $?
