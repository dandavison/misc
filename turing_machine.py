import sys
from collections import deque

from toolz import take


class Machine:

    def __init__(self, rules):
        self.rules = rules
        self.deque = deque([])
        self.pos = self.left_end = self.right_end = None
        self.mconfig = None

    def initialize(self, symbols):
        self.deque.append(symbols[0])
        self.right_end = self.left_end = self.pos = 0
        for symbol in symbols[1:]:
            self.deque.append(symbol)
            self.go_right()
        self.mconfig = "b"

    def execute(self):
        while True:
            current_symbol = self.read()
            ops, self.mconfig = self.rules[self.mconfig, current_symbol]
            for op in ops:
                if op.startswith('P'):
                    _, output = op
                    yield output
                else:
                    self.do_operation(op)

    def do_operation(self, operation):
        return {
            'L': self.go_left,
            'R': self.go_right,
        }[operation]()

    def read(self):
        return self.deque[self.pos]

    def write(self, symbol):
        self.deque[self.pos] = symbol

    def go_left(self):
        if self.pos == self.left_end:
            self.deque.appendleft(' ')
            self.left_end -= 1
        self.pos -= 1

    def go_right(self):
        if self.pos == self.right_end:
            self.deque.append(' ')
            self.right_end += 1
        self.pos += 1


def parse_rules(fp):
    return dict(map(parse_rule, fp))


def parse_rule(line):
    mconfig, symbol, operations, mconfig_next = line.strip().split()
    if symbol == 'None':
        symbol = ' '
    operations = operations.split(',')
    config = mconfig, symbol
    behaviour = operations, mconfig_next
    return config, behaviour


if __name__ == '__main__':
    [rules_path] = sys.argv[1:]
    with open(rules_path) as fp:
        rules = parse_rules(fp)
    machine = Machine(rules)
    machine.initialize(" ")
    print(''.join(take(100, machine.execute())))
