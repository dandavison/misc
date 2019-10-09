# 3blue1brown pi in colliding blocks
# https://www.youtube.com/watch?v=HEfHFsfGXjs
import sys
from dataclasses import dataclass
from typing import Tuple

VERBOSE = False


@dataclass
class Blocks:
    m0 = 1.0  # mass of left block
    m1 = None  # mass of right block (read from argv)

    v0 = 0.0  # left block starts off stationary

    v1 = -1.0  # initial velocity of right block

    def will_collide_again(self):
        return abs(self.v0) > self.v1

    def collide(self):
        v0, v1 = self.v0, self.v1
        m0, m1 = self.m0, self.m1
        self.v0 = (m0 * v0 - m1 * v0 + 2 * m1 * v1) / (m0 + m1)
        self.v1 = (2 * m0 * v0 - m0 * v1 + m1 * v1) / (m0 + m1)

    def print(self):
        if VERBOSE:
            print(f"{self.v0:.2f} {self.v1:.2f}")


if __name__ == "__main__":
    assert not sys.argv[2:]

    blocks = Blocks()
    blocks.m1 = float(sys.argv[1])

    n = 0
    while True:
        blocks.print()
        blocks.collide()
        blocks.print()
        n += 1
        if blocks.will_collide_again():
            # Bounce off wall
            blocks.v0 = -blocks.v0
            n += 1
        else:
            break

    if blocks.v0 < 0:
        # Bounce off wall
        n += 1

    print(n)
