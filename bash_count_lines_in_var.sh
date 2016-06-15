#!/bin/bash
# http://stackoverflow.com/questions/23736555/correctly-count-number-of-lines-a-bash-variable

count_it() {
    echo "Variablie contains $2: ==>$1<=="
    echo -n 'grep:'; echo -n "$1" | grep -c '^'
    echo -n 'grep <<<:'; grep -c '^' <<< "$1"
    echo -n 'wc  :'; echo -n "$1" | wc -l
    echo
}

VAR=''
count_it "$VAR" "empty variable"

VAR='one line'
count_it "$VAR" "one line without \n at the end"

VAR='line1
'
count_it "$VAR" "one line with \n at the end"

VAR='line1
line2'
count_it "$VAR" "two lines without \n at the end"

VAR='line1
line2
'
count_it "$VAR" "two lines with \n at the end"
