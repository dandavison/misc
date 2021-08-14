squares = []
for x in range(5):
    squares.append((lambda arg: lambda: arg**2)(x))

squares[2]()
squares[4]()


def squarer(x):
    return lambda: x**2

squarers = [squarer(x) for x in range(5)]
