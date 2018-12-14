from dataclasses import dataclass

from itertools import cycle
from itertools import starmap

import numpy as np


def parse_input(fp):
    return np.array([list(line.strip('\n')) for line in fp])


SYMBOL_2_DIRECTION = {
    'v': +1 + 0j,
    '>': +0 + 1j,
    '^': -1 + 0j,
    '<': +0 - 1j,
}

@dataclass
class Cart:
    location: complex
    direction: complex

    INTERSECTION_DIRECTIONS = [1j, 1, -1j]
    n_intersections: int = 0

    @property
    def next_intersection_direction(self):
        return self.INTERSECTION_DIRECTIONS[self.n_intersections % 3]

    def get_turn_direction(self, track):
        """
        |    | \  | /  |
        |----+----+----|
        |  1 | -j | j  |
        |  j | j  | -j |
        | -1 | -j | j  |
        | -j | j  | -j |
        """
        return {
            '\\': {1: -1j, 1j: 1j, -1: -1j, -1j: 1j},
            '/': {1: 1j, 1j: -1j, -1: 1j, -1j: -1j},
        }[track][self.direction]

    @property
    def track_symbol(self):
        """
        The track symbol that would be present if the cart symbol wasn't there.
        """
        return '|' if self.direction.real else '-'


class State:

    def __init__(self, array, carts=None):
        self.array = array
        self.carts = self._get_carts() if carts is None else carts
        for cart in self.carts:
            self[cart.location] = cart.track_symbol

    def _get_carts(self):
        return sorted((Cart(location, SYMBOL_2_DIRECTION[self[location]])
                       for location in self.cart_locations),
                      key=lambda c: (c.location.real, c.location.imag))

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
        self = State(self.array.copy(), self.carts)
        for cart in self.carts:
            self[cart.location] = invert_dict(SYMBOL_2_DIRECTION)[cart.direction]
        print('\n' + '\n'.join(''.join(row) for row in self.array) + '\n')


def evolve(state, n_generations):
    for gen in range(n_generations):
        for cart in state.carts:
            print(f'cart at {cart.location} has track {cart.track_symbol}, direction {cart.direction}, turn {cart.n_intersections}')
            cart.location += cart.direction
            track = state[cart.location]
            if track == '+':
                cart.direction *= cart.next_intersection_direction
                cart.n_intersections += 1
            elif track in '\/':
                cart.direction *= cart.get_turn_direction(track)
        state.print()


def invert_dict(d):
    return {v: k for k, v in d.items()}


with open('/tmp/13.txt') as fp:
    state = State(parse_input(fp))

state.print()
evolve(state, 3)
