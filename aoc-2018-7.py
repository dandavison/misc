from collections import defaultdict
from itertools import chain


def read_edges(fp):
    return [
        (words[1], words[7])
        for line in fp
        for words in [line.strip().split()]
    ]


def make_adjacency_list(edges):
    adjacency_list = defaultdict(list)
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v] = []
    return dict(adjacency_list)


def topological_sort(graph):
    graph = graph.copy()
    nodes = []
    while True:
        children = set(chain.from_iterable(graph.values()))
        nodes_without_dependencies = graph.keys() - children
        if not nodes_without_dependencies:
            return nodes
        else:
            next_node = min(nodes_without_dependencies)
            nodes.append(next_node)
            del graph[next_node]


from sys import stdin
graph = make_adjacency_list(read_edges(stdin))
print(graph)
# part 1
print(topological_sort(graph))
