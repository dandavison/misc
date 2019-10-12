# 3blue1brown pi in colliding blocks
# https://www.youtube.com/watch?v=HEfHFsfGXjs
import sys
from dataclasses import dataclass


@dataclass
class Blocks:
    m1 = None  # mass of right block (supplied as input)
    m2 = 1.0  # mass of left block

    v1 = -1.0  # initial velocity of right block
    v2 = 0.0  # left block starts off stationary

    def will_collide_again(self):
        return abs(self.v2) > self.v1

    def collide(self):
        v1, v2 = self.v1, self.v2
        m1, m2 = self.m1, self.m2
        self.v1 = (2 * m2 * v2 + v1 * (m1 - m2)) / (m2 + m1)
        self.v2 = (2 * m1 * v1 - v2 * (m1 - m2)) / (m2 + m1)

    def simulate(self):
        n = 0
        while True:
            self.collide()
            n += 1
            if self.will_collide_again():
                # Bounce off wall
                self.v2 = -self.v2
                n += 1
            else:
                break
        if self.v2 < 0:
            # Bounce off wall
            n += 1
        print(n)


if __name__ == "__main__":
    assert not sys.argv[2:]
    blocks = Blocks()
    blocks.m1 = float(sys.argv[1])
    blocks.simulate()
