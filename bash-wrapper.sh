#!/bin/bash
log=/tmp/bash-wrapper.log
date >> $log
echo "bash-wrapper" >> $log
echo "$@" >> $log
echo >> $log
exec bash "$@"
