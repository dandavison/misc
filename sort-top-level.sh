#!/bin/bash
marker='__@marker@__'
sed -n "s,\n,$marker,g"
