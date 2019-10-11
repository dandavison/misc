# 3blue1brown pi in colliding blocks
# https://www.youtube.com/watch?v=HEfHFsfGXjs
import sys
from dataclasses import dataclass
from typing import Tuple


@dataclass
class Blocks:
    m1 = 1.0  # mass of left block
    m2 = None  # mass of right block (supplied as input)

    v1 = 0.0  # left block starts off stationary
    v2 = -1.0  # initial velocity of right block

    def will_collide_again(self):
        return abs(self.v1) > self.v2

    def collide(self):
        v1, v2 = self.v1, self.v2
        m1, m2 = self.m1, self.m2
        self.v1 = (2 * m2 * v2 - v1 * (m2 - m1)) / (m1 + m2)
        self.v2 = (2 * m1 * v1 + v2 * (m2 - m1)) / (m1 + m2)

    def simulate(self):
        n = 0
        while True:
            self.collide()
            n += 1
            if self.will_collide_again():
                # Bounce off wall
                self.v1 = -self.v1
                n += 1
            else:
                break
        if self.v1 < 0:
            # Bounce off wall
            n += 1
        print(n)


if __name__ == "__main__":
    assert not sys.argv[2:]
    blocks = Blocks()
    blocks.m2 = float(sys.argv[1])
    blocks.simulate()
