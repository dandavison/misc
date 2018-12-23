from dataclasses import dataclass

from collections import Counter
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
        |  j | -j | j  |
        |  1 | j  | -j |
        | -j | -j | j  |
        | -1 | j  | -j |
        """
        return {
            '\\': {1j: -1j, 1:  1j, -1j: -1j, -1:  1j},
            '/':  {1j:  1j, 1: -1j, -1j:  1j, -1: -1j},
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

    @property
    def collisions(self):
        return [index
                for index, n in Counter(self._get_index(cart.location) for cart in self.carts).items()
                if n > 1]

    def print(self):
        return
        self = State(self.array.copy(), self.carts)
        for cart in self.carts:
            self[cart.location] = invert_dict(SYMBOL_2_DIRECTION)[cart.direction]
        print('\n' + '\n'.join(''.join(row) for row in self.array) + '\n')


def evolve(state, n_generations):
    state.print()
    for gen in range(1, n_generations + 1):

        for cart in list(state.carts):
            if state._get_index(cart.location + cart.direction) in {state._get_index(c.location) for c in state.carts}:
                state.carts = [c for c in state.carts
                               if state._get_index(c.location) != state._get_index(cart.location + cart.direction)]
                print(f'collisions in generation {gen}. {len(state.carts)} carts left.')

            else:
                cart.location += cart.direction
                track = state[cart.location]
                if track == '+':
                    cart.direction *= cart.next_intersection_direction
                    cart.n_intersections += 1
                elif track in '\/':
                    cart.direction *= cart.get_turn_direction(track)

        if len(state.carts) == 1:
            state.print()
            [cart] = state.carts
            return state._get_index(cart.location)

        state.print()


def invert_dict(d):
    return {v: k for k, v in d.items()}


path = '/Users/dan/tmp/aoc-2018/input/13.txt'
# path = '/tmp/13.txt'
# path = '/tmp/in'
with open(path) as fp:
    state = State(parse_input(fp))

print(evolve(state, 10000000))


# (You guessed 137,54.)
# You guessed 146,110.
