#!/usr/bin/env python
import readline
readline.parse_and_bind('tab: menu-complete')
def complete(text, state):
    options = ['a', 'b']
    return options[state]
readline.set_completer(complete)
raw_input()
