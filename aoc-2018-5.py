from functools import reduce


def part1(polymer):
    return len(react(polymer))


def react(polymer):
    return reduce(cons, list(polymer), [])


def cons(xs, y):
    if not xs:
        return [y]
    *xs, x = xs
    if x.lower() == y.lower() and x != y:
        return xs
    else:
        return xs + [x] + [y]


if __name__ == '__main__':
    import sys
    polymer = sys.stdin.read().rstrip()
    print(part1(polymer))
