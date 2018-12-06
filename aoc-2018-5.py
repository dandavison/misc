import sys


def part1(polymer):
    return len(react(polymer))


def react(polymer):
    while True:
        i = get_index_of_reactive_pair(polymer)
        if i is None:
            return polymer
        else:
            polymer = polymer[:i] + polymer[i+2:]


def get_index_of_reactive_pair(polymer):
    assert len(polymer) > 1
    prev = polymer[0]
    for i in range(1, len(polymer)):
        curr = polymer[i]
        if prev.lower() == curr.lower():
            if (prev.islower() and curr.isupper() or
                prev.isupper() and curr.islower()):
                return i - 1
        prev = curr
    return None


if __name__ == '__main__':
    polymer = sys.stdin.read().rstrip()
    print(part1(polymer))
