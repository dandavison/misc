#!/usr/bin/env python
import re
import subprocess
import sys

import networkx as nx
from networkx.drawing.nx_pydot import write_dot


def parse_function_definition(line):
    if (match := re.match(r"^\(defun (xenops-[^ ]+)", line)) :
        return match.group(1)


def parse_call(line):
    # TODO: parse multiple on a single line
    if (match := re.match(r"[ \t]+.*\((xenops-[^ )]+)", line)) :
        return match.group(1)


def create_call_graph(files):
    grep_output = subprocess.check_output(
        ["rg", "-N", "--no-filename", r"(\(defun|\(xenops-)"] + files
    )
    graph = nx.DiGraph()
    caller = None
    for line in grep_output.decode("utf-8").splitlines():
        print(line)
        if (next_caller := parse_function_definition(line)) is None:
            callee = parse_call(line)
            if not callee:
                continue
            print("    " + callee)
            graph.add_edge(caller, callee)
        else:
            caller = next_caller
            print(caller)

    return graph


def visualize(graph):
    write_dot(graph, "/tmp/graph.dot")
    subprocess.check_call(["dot", "-T", "svg", "-o", "graph.svg", "/tmp/graph.dot"])


if __name__ == "__main__":
    _, *files = sys.argv
    visualize(create_call_graph(sorted(files)))
