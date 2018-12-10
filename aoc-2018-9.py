from collections import defaultdict


def play(n_players, last_marble):
    circle = [0, 1]
    curr = 1
    scores = defaultdict(int)
    for i in range(2, last_marble):
        if i != 23:
            insertion = (curr + 2) % len(circle)
            circle = circle[:insertion] + [i] + circle[insertion:]
            curr = insertion
        else:
            player = i % n_players
            removed = (curr - 7) % len(circle)
            scores[player] += i + removed
            del circle[removed]
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
    print(play(n_players, last_marble), expected)
