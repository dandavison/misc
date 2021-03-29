#!/bin/bash

# https://unix.stackexchange.com/questions/88296/get-vertical-cursor-position/183121#183121
IFS=';' read -sdR -p $'\x1b[6n' ROW COL; echo "${ROW#*[}"


# https://iterm2.com/documentation-escape-codes.html
# ^[]4;-2;?^G

# Getting close
read -s -N 25 -p $'\x1b]4;-2;?\x07' RESPONSE

# Less close
read -sdr -p $'\x1b]4;-2;?\x07' RESPONSE; echo "${RESPONSE#*[}"
