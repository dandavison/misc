from collections import defaultdict
from itertools import chain
from string import ascii_uppercase

from toolz import unique


def read_edges(fp):
    return [
        (words[1], words[7])
        for line in fp
        for words in [line.strip().split()]
    ]


def make_adjacency_list(edges):
    adjacency_list = defaultdict(list)
    for u, v in edges:
        adjacency_list[u].extend([v])
        adjacency_list[v].extend([])
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


class Worker:
    def __init__(self, label):
        self.label = label
        self.time2task = {}

    def __str__(self):
        return f'Worker({self.label})'

    def is_available(self, time):
        return time not in self.time2task


class Scheduler:
    def __init__(self, dependency_graph, n_workers, base_time):
        self.dependency_graph = dependency_graph.copy()
        self.workers = [Worker(i) for i in range(n_workers)]
        self.base_time = base_time
        self.current_time = 1
        self.task_sequence = []

    @property
    def tasks(self):
        return self.dependency_graph.keys()

    @property
    def tasks_without_dependencies(self):
        return self.tasks - self.tasks_with_dependecies

    @property
    def tasks_with_dependecies(self):
        return set(chain.from_iterable(self.dependency_graph.values()))

    @property
    def final_task_end_time(self):
        return max(chain.from_iterable(w.time2task for w in self.workers))

    @property
    def available_workers(self):
        return [w for w in self.workers if w.is_available(self.current_time)]

    def consume_tasks(self):
        min_end_time = None

        assignable_tasks = list(zip(sorted(self.tasks_without_dependencies), self.available_workers))

        if not assignable_tasks:
            return False

        for task, worker in assignable_tasks:
            end_time = self.current_time + self.task_duration(task)
            min_end_time = min(min_end_time, end_time) if min_end_time is not None else end_time
            for t in range(self.current_time, end_time):
                worker.time2task[t] = task
                self.task_sequence.append(task)
            del self.dependency_graph[task]

        assert min_end_time is not None
        self.current_time = min_end_time

        return True

    def task_duration(self, task):
        return self.base_time + 1 + ascii_uppercase.index(task)


def total_time(dependency_graph, n_workers, base_time):
    scheduler = Scheduler(dependency_graph, n_workers, base_time)
    while scheduler.consume_tasks():
        pass
    return scheduler.final_task_end_time


def task_sequence(dependency_graph, n_workers=1, base_time=0):
    scheduler = Scheduler(dependency_graph, n_workers=n_workers, base_time=base_time)
    while scheduler.consume_tasks():
        pass
    return ''.join(map(str, unique(scheduler.task_sequence)))


from sys import stdin

for path, n_workers, base_time, expected_order in [
        ("/tmp/7.txt", 2, 0, "CABDFE"),
        ("/Users/dan/tmp/aoc-2018/input/07.txt", 5, 60, "OKBNLPHCSVWAIRDGUZEFMXYTJQ"),
]:
    with open(path) as fp:
        graph = make_adjacency_list(read_edges(fp))
    print(sorted((k, ''.join(sorted(v))) for k, v in graph.items()))

    # part 1
    topo_sort_order = ''.join(topological_sort(graph))
    assert topo_sort_order == expected_order
    assert task_sequence(graph, n_workers=1) == expected_order
    assert task_sequence(graph, n_workers=1, base_time=60) == expected_order
    print(topo_sort_order)

    # part 2
    print(task_sequence(graph, n_workers=n_workers))
    print(total_time(graph, n_workers=n_workers, base_time=base_time))