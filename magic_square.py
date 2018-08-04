class Square:

    def __init__(self, values, cost):
        self.values = values
        self.cost = cost

    @classmethod
    def from_rows(self, rows):
        self.values = {
            (i, j): rows[i][j]
            for i in range(3)
            for j in range(3)
        }
        self.cost = 0

    def transform(self, x, y):
        values = self.values.copy()
        for k, v in values.items():
            if v == x:
                values[k] = y

        return Square(values, self.cost + abs(y - x))

    def row(self, i):
        return [self.values[i, j] for j in range(3)]

    def col(self, j):
        return [self.values[i, j] for i in range(3)]

    def diag1(self):
        return [self.values[i, j] for i, j in zip(range(3), range(3))]

    def diag2(self):
        return [self.values[i, 2 - j] for i, j in zip(range(3), range(3))]

    def is_magic(self):
        return (self.row(0) == self.row(1) == self.row(2) ==
                self.col(0) == self.col(1) == self.col(2) ==
                self.diag1() == self.diag2())

    def __hash__(self):
        # TODO: squares that are equivalent up to rotational symmetry should have the same hash
        # value.
        return hash(tuple(sorted(self.values.items())))


class Tree:

    def __init__(self, root):
        self.root = root
        self.min_cost = float('inf')
        self.node_cache = {}

    def add_layer(self):
        for node in self.get_layer(self.depth):
            if node.cost < self.min_cost:
                for x in range(1, 10):
                    for y in range(1, 10):
                        if y != x:
                            child = node.transform(x, y)
                            child = self.node_cache.set_default(hash(child), child)






def solve(square):

    min_cost = float('inf')

    tree = Tree(square)

    while True:


    if square.is_magic():
        if square.cost < min_cost:
            min_cost = square.cost


if __name__ == '__main__':
    square = Square([(1, 2, 3),
                     (4, 5, 6),
                     (7, 8, 9)])
    print(solve(square))
