from dataclasses import dataclass

from itertools import cycle

import numpy as np


def parse_input(fp):
    return np.array([list(line.strip('\n')) for line in fp])


CART_SYMBOLS = [('>', 1), ('v', -1j), ('^', 1j), ('<', -1)]
TURNS = cycle([1j, 1, -1j])


@dataclass
class Cart:
    location: complex
    direction: complex


@dataclass
class State:
    array: np.array

    def __getitem__(self, index):
        return self.array[self._get_index(index)]

    def __setitem__(self, index, value):
        self.array[self._get_index(index)] = value

    @staticmethod
    def _get_index(index):
        return int(index.real), int(index.imag)

    def print(self):
        print()
        print('\n'.join(''.join(row) for row in self.array))
        print()


def evolve(state, n_generations):
    carts = []
    for sym, direction in CART_SYMBOLS:
        for location in np.where(state == sym):
            location = complex(*tuple(location))
            carts.append(Cart(location, direction))
            state[location] = '|' if location.real else '-'

    carts.sort(key=lambda c: (c.location.real, c.location.imag))

    for gen in range(n_generations):
        for cart in carts:
            state[cart.location] = '|' if cart.location.real else '-'
            cart.location += cart.direction
            if state[cart.location] == '+':
                cart.direction *= TURNS[cart.n_turns]
                cart.location += cart.direction
                cart.n_turns += 1
            state[cart.location] = next(sym for sym, direction in CART_SYMBOLS
                                        if direction == cart.direction)

        state.print()


with open('/tmp/13.txt') as fp:
    state = State(parse_input(fp))

state.print()
evolve(state, 2)
