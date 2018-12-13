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
        return self.array[int(index.real), int(index.imag)]

    def print(self):
        print()
        print('\n'.join(''.join(row) for row in self.array))
        print()


def evolve(state, n_generations):
    carts = []
    for sym, direction in CART_SYMBOLS:
        for location in np.where(state == sym):
            carts.append(Cart(complex(*tuple(location)), direction))

    carts.sort(key=lambda c: (c.location.real, c.location.imag))

    for gen in range(n_generations):
        for cart in carts:
            cart.location += cart.location + cart.direction
            if state[cart.location] == '+':
                cart.direction *= TURNS[cart.n_turns]
                cart.n_turns += 1

        state.print()


with open('/tmp/13.txt') as fp:
    state = State(parse_input(fp))

state.print()
evolve(state, 2)
