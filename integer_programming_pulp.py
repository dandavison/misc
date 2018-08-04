from pulp import LpInteger
from pulp import LpMinimize
from pulp import LpProblem
from pulp import LpVariable
from pulp import LpStatus


make_integers(['x1', 'x2', 'x3', 'x4'])


def make_integers(names):
    variables = [LpVariable(name, 0, 1, LpInteger) for name in names]
    globals().update(zip(names, variables))


def problem_1():
    problem = LpProblem('problem_1', LpMinimize)

    # TODO: what should the objective function be if I am only interested in finding values that
    # satisfy the constraints?
    problem += x1 + x2 + x3

    problem += x1 + x2 == 0
    problem += x2 + x3 == 0
    problem += x1 + x3 == 0

    status = problem.solve()
    assert LpStatus[status] == 'Optimal'

    solution = {v.name: v.varValue for v in problem.variables()}
    assert solution == {'x1': 0.0, 'x2': 0.0, 'x3': 0.0}
    return solution


def problem_2():
    problem = LpProblem('problem_1', LpMinimize)

    # TODO: what should the objective function be if I am only interested in finding values that
    # satisfy the constraints?
    problem += x1 + x2 + x3

    problem += x1 + x2 == 0
    problem += x2 + x3 == 1

    status = problem.solve()
    assert LpStatus[status] == 'Optimal'

    solution = {v.name: v.varValue for v in problem.variables()}
    assert solution == {'x1': 0.0, 'x2': 0.0, 'x3': 1.0}
    return solution


def problem_3():
    make_integers(['x1', 'x2', 'x3', 'x4'])
    problem = LpProblem('problem_1', LpMinimize)

    # TODO: what should the objective function be if I am only interested in finding values that
    # satisfy the constraints?
    problem += x1 + x2 + x3 + x4

    problem += x1 + x2 == 0
    problem += x2 + x3 == 1
    problem += x2 + x4 == 0
    problem += x3 + x4 == 0

    status = problem.solve()
    assert LpStatus[status] == 'Optimal'

    solution = {v.name: v.varValue for v in problem.variables()}
    # assert solution == {'x1': 0.0, 'x2': 0.0, 'x3': 1.0, 'x4': 0.0}
    return solution
