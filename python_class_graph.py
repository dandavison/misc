import os

import networkx as nx
from networkx.drawing.nx_pydot import write_dot


def make_graph(classes):
    graph = nx.DiGraph()
    for cls in classes:
        graph.add_path(reversed([_cls.__name__ for _cls in cls.mro() if not _cls.__name__.endswith('Mixin')]))
    return graph


def visualize(graph):
    write_dot(graph, '/tmp/graph.dot')
    os.system('dot -T svg -o /tmp/graph.svg /tmp/graph.dot')


