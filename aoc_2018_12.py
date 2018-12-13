import numpy as np
from toolz import compose

from clint.textui import colored
green = lambda s: colored.green(s, bold=True)
red = lambda s: colored.red(s, bold=True)


np.set_printoptions(linewidth=np.inf)


def parse_plant_sequence(s):
    return np.array([{'#': 1, '.': 0}[c] for c in s])


def parse_rule_line(line):
    input, output = map(compose(parse_plant_sequence, str.strip), line.strip().split('=>'))
    [output] = output
    return input, output


def parse_input(fp):
    first_line = next(fp).strip()
    initial_text = 'initial state: '
    assert first_line.startswith(initial_text)
    initial_state = parse_plant_sequence(first_line[len(initial_text):].strip())
    assert not next(fp).strip()
    rules = [parse_rule_line(line) for line in fp]
    initial_state = np.concatenate([np.zeros_like(initial_state),
                                    initial_state,
                                    np.zeros_like(initial_state)])
    return initial_state, rules


def evolve(state, rules, n_generations):
    _rules = [(tuple(p), y) for p, y in rules]
    assert len(set(_rules)) == len(_rules)
    for _ in range(n_generations):
        matched = set()
        next_state = state.copy()
        for i in range(2, len(state) - 3):
            window = state[i-2:i+3]
            for pattern, yields_plant in rules:
                if np.all(window == pattern):
                    if False:
                        print(f'rule {pattern} matched plant {plant - len(state)//3}: {next_state[plant]} -> {yields_plant}')
                    assert i not in matched
                    matched.add(i)
                    next_state[i] = yields_plant
                    break  # patterns are distinct so there can be no more matches for this window
            else:
                # print('No matching pattern')
                assert False
                next_state[i] = 0

        # print(green(next_state))

        state = next_state
    return state


with open('/Users/dan/tmp/aoc-2018/input/12.txt') as fp:  # /tmp/12.txt
    initial_state, rules = parse_input(fp)


print(initial_state)
print(np.sum(np.nonzero(evolve(initial_state, rules, 20))[0] - len(initial_state) // 3))
