#!/usr/bin/env python3

TERMINATOR = '$'


class Trie:

    def __init__(self):
        self.root = {}

    def add_word(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[TERMINATOR] = None

    def is_word(self, word):
        node = self._get_node(word)
        return node and TERMINATOR in node

    def is_prefix(self, string):
        return self._get_node(string) is not None

    def _get_node(self, string):
        node = self.root
        for c in string:
            node = node.get(c)
            if node is None:
                return None
        return node


if __name__ == '__main__':
    t = Trie()
    t.add_word('fish')
    t.add_word('trombone')
    t.add_word('rex')
    assert t.is_word('rex')
    assert t.is_prefix('trom')
    assert not t.is_word('rexs')
