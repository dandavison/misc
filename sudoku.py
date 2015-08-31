from collections import Counter
from collections import defaultdict

import numpy as np


class Sudoku(object):

    def __init__(self, cells, twist):
        self.cells = np.array([[set(range(1, 10)) for i in range(9)]
                               for j in range(9)])
        self.twist = twist

        for index, value in cells.items():
            self.cells[index] = {value}

        self.verbose = False

    def solve(self):

        it = 0

        hash_0 = hash(self)
        while True:

            for i in range(9):
                self.eliminate(self.cells[i, :])

            for j in range(9):
                self.eliminate(self.cells[:, j])

            for i in range(3):
                for j in range(3):
                    self.eliminate(self.get_block(i, j).ravel())

            self.eliminate(self.get_twist_cells())

            it += 1

            if all(len(values) == 1 for values in self.cells.ravel()):
                print 'solved! (iteration %d)' % it
                return self

            hash_1 = hash(self)
            if hash_0 == hash_1:
                raise RuntimeError("Failed: grid unaltered")
            hash_0 = hash_1

            if it == 100:
                raise RuntimeError(
                    "Failed: %d iterations with no solution" % it)

    def eliminate(self, cells):

        # Find all determined values and create a map from values to possible
        # cells.
        determined = set()
        values2cells = defaultdict(set)
        for k, values in enumerate(cells):
            if len(values) == 1:
                [value] = values
                assert value not in determined
                determined.update(values)
            for value in values:
                values2cells[value].add(k)

        # Assign values that have only one possible cell
        for value, _cells in values2cells.items():
            if len(_cells) == 1:
                [cell] = _cells
                cells[cell].clear()
                cells[cell].add(value)

        # Remove determined values from the set of possibilities in other cells
        for values in cells:
            if len(values) > 1:
                values -= determined

    def get_twist_cells(self):
        return [self.cells[index] for index in self.twist]

    def get_block(self, i, j):
        rows = [k for k in range(9) if k / 3 == i]
        columns = [k for k in range(9) if k / 3 == j]
        row_slice = slice(min(rows), max(rows) + 1)
        column_slice = slice(min(columns), max(columns) + 1)
        return self.cells[row_slice, column_slice]

    def counts(self):
        return Counter(map(len, self.cells.ravel()))

    def size(self):
        return sum(map(len, self.cells.ravel()))

    def __hash__(self):
        data = tuple(map(tuple, self.cells.ravel()))
        return hash(data)

    def __repr__(self):
        chars = ''
        for i in range(9):
            for j in range(9):
                if len(self.cells[i, j]) == 1:
                    [value] = self.cells[i, j]
                    chars += str(value)
                else:
                    chars += '.'
                chars += ' '
            chars += '\n'
        return chars



if __name__ == '__main__':
    cells = {
        (0, 1): 9,
        (0, 2): 1,
        (0, 7): 6,

        (1, 0): 8,
        (1, 5): 9,
        (1, 6): 1,
        (1, 8): 4,

        (2, 1): 5,
        (2, 4): 1,
        (2, 5): 8,
        (2, 8): 3,

        (3, 1): 7,
        (3, 2): 6,

        (4, 2): 8,
        (4, 6): 2,

        (5, 6): 6,
        (5, 7): 7,

        (6, 0): 1,
        (6, 3): 9,
        (6, 4): 3,
        (6, 7): 4,

        (7, 0): 3,
        (7, 2): 5,
        (7, 3): 4,
        (7, 8): 7,

        (8, 1): 2,
        (8, 6): 3,
        (8, 7): 8,

    }
    twist = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 3),
        (5, 4),
        (6, 5),
        (7, 4),
        (8, 5),
    ]
    sudoku = Sudoku(cells, twist)
    print sudoku
    print sudoku.solve()
