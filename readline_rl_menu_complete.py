#!/usr/bin/env python
import rl

def complete(text):
    return ['a', 'b']

rl.completer.parse_and_bind('tab: menu-complete')
rl.completer.completer = rl.generator(complete)
raw_input()
