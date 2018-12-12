from collections import defaultdict
from collections import deque


def play(n_players, last_marble):
    circle = deque([0])
    scores = defaultdict(int)
    for i in range(1, last_marble + 1):

        player = (i % n_players) or n_players

        if i and i % 23 == 0:
            circle.rotate(-7)
            removed = circle.pop()
            scores[player] += i + removed
        else:
            circle.rotate(2)
            circle.append(i)

        if False:
            print('{i} [{player}] {circle}'.format(
                i=i,
                player=player,
                circle=''.join(('%-3d' if m != circle[0] else '(%d)') % m for m in circle),
            ))

    return max(scores.values())


test_games = [
    (9, 25, 32),
    (10, 1618, 8317),
    (13, 7999, 146373),
    (17, 1104, 2764),
    (21, 6111, 54718),
    (30, 5807, 37305),
]

for n_players, last_marble, expected  in test_games:
    assert play(n_players, last_marble) == expected

print(play(466, 71436))
print(play(466, 100 * 71436))
