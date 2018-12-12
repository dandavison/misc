from collections import defaultdict


class Circle:

    def __init__(self, shard_size=1e5):
        self.shards = [[]]

    def _get_shard_and_index(self, index):
        offset = 0
        for shard in self.shards:
            if offset + len(shard) >= index:
                return shard, index - offset
            else:
                offset += len(shard)

    def insert(self, index, obj):
        shard, index = self._get_shard_and_index(index)
        shard.insert(index, obj)

    def __getitem__(self, index):
        shard, index = self._get_shard_and_index(index)
        return shard[index]

    def __delitem__(self, index):
        shard, index = self._get_shard_and_index(index)
        del shard[index]


def play(n_players, last_marble):
    circle = [0]
    curr = 0
    scores = defaultdict(int)
    for i in range(1, last_marble + 1):

        if i % 10000 == 0:
            print(f'{i}/{last_marble}')

        player = (i % n_players) or n_players

        if i and i % 23 == 0:
            removed = (curr - 7) % len(circle)
            scores[player] += i + circle[removed]
            del circle[removed]
            curr = removed
        else:
            insertion = ((curr + 2) % len(circle)) or len(circle)
            circle.insert(insertion, i)  # splicing the list is much slower
            curr = insertion

        if False:
            print('{i} [{player}] {circle}'.format(
                i=i,
                player=player,
                circle=''.join(('%-3d' if m != circle[curr] else '(%d)') % m for m in circle),
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
