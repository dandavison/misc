from dataclasses import dataclass

from itertools import cycle
from itertools import starmap

import numpy as np


def parse_input(fp):
    return np.array([list(line.strip('\n')) for line in fp])


SYMBOL_2_DIRECTION = {
    '>': +1 + 0j,
    '^': +0 + 1j,
    '<': -1 + 0j,
    'v': +0 - 1j,
}

TURNS = cycle([1j, 1, -1j])


@dataclass
class Cart:
    location: complex
    direction: complex

    def track_symbol(self):
        """
        The track symbol that would be present if the cart symbol wasn't there.
        """
        return '|' if self.direction.real else '-'


@dataclass
class State:
    array: np.array

    @property
    def cart_locations(self):
        return list(starmap(complex,
                            np.transpose(np.where(np.isin(self.array, list(SYMBOL_2_DIRECTION))))))

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

    for location in state.cart_locations:
        direction = SYMBOL_2_DIRECTION[state[location]]
        carts.append(Cart(location, direction))

    carts.sort(key=lambda c: (c.location.real, c.location.imag))

    for gen in range(n_generations):
        for cart in carts:
            state[cart.location] = '|' if cart.location.real else '-'

            print(f'cart at {cart.location} has track {state[cart.location]} and direction {cart.direction}')

            cart.location += cart.direction
            if state[cart.location] == '+':
                cart.direction *= TURNS[cart.n_turns]
                cart.location += cart.direction
                cart.n_turns += 1
            state[cart.location] = invert_dict(SYMBOL_2_DIRECTION)[cart.direction]

        state.print()


def invert_dict(d):
    return {v: k for k, v in d.items()}


with open('/tmp/13.txt') as fp:
    state = State(parse_input(fp))

state.print()
evolve(state, 2)
