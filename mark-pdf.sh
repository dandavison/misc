#!/bin/bash
# -*- coding: utf-8 -*-

file="$1"
mark="%ÓÓ"
echo "$file"
# Unmark
# ggrep -q "$mark" "$file" && sed -i -e "s/ $mark//" "$file"
ggrep -q "^$mark$" "$file" || sed -i "1 a $mark" "$file"
