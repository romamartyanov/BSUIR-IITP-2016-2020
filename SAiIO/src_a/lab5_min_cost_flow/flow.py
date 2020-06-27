import numpy as np
import sympy as sp
from sympy.solvers.solveset import linsolve
from pprint import pprint


def get_cycle(basis_indexes, start, finish):
    used = [False for i in range(len(basis_indexes))]

    def dfs(basis_indexes, start, finish):
        straight = []
        reverse = []

        if start == finish:
            return straight, reverse

        for i, (from_, to_) in enumerate(basis_indexes):
            if used[i]:
                continue

            if from_ == start:
                used[i] = True
                res = dfs(basis_indexes, to_, finish)
                if res:
                    straight.append((from_, to_))
                    straight += res[0]
                    reverse += res[1]
                    return straight, reverse

            if to_ == start:
                used[i] = True
                res = dfs(basis_indexes, from_, finish)
                if res:
                    reverse.append((from_, to_))
                    straight += res[0]
                    reverse += res[1]
                    return straight, reverse

    straight, reverse = dfs(basis_indexes, start, finish)
    straight.append((finish, start))

    return straight, reverse


def get_c(costs, i, j):
    for to, cost in costs[i]:
        if to == j:
            return cost


def get_u(costs, basis):
    n = len(costs)
    u = np.zeros(n)
    used = [False for _ in range(n)]
    used[0] = True

    while not all(used):
        for i, j in basis:
            if used[i]:
                u[j] = u[i] - get_c(costs, i, j)
                used[j] = True
            elif used[j]:
                u[i] = u[j] + get_c(costs, i, j)
                used[i] = True

    return u


def min_cost_edge(edges):
    min_x = 1e9
    min_pair = None

    for from_, to_ in edges:
        cost = get_c(x, from_, to_)
        if cost < min_x:
            min_x = cost
            min_pair = (from_, to_)

    return min_x, min_pair


def get_not_basis(graph, basis):
    not_basis_edges = []
    for src, dests in enumerate(graph):
        for dest in dests:
            if (src, dest) not in basis:
                not_basis_edges.append((src, dest))
    return not_basis_edges


def get_delta(costs, u, not_basis_edges):
    delta = []
    for i, j in not_basis_edges:
        delta.append(u[i] - u[j] - get_c(costs, i, j))
    return delta


def get_bad_edge(costs, u, not_basis_edges):
    for i, j in not_basis_edges:
        if u[i] - u[j] - get_c(costs, i, j) > 0:
            return (i, j)

    return None


def run(costs, basis_indexes, x):
    graph = []
    for d in costs:
        g = []
        for e in d:
            g.append(e[0])
        graph.append(g)

    print('X array:', x)
    print('Graph:', graph)
    print('b', basis_indexes)
    print()

    count = 0
    while True:
        count += 1
        print('\nIter', count)

        u = get_u(costs, basis_indexes)
        print('u', u)

        not_basis_edges = get_not_basis(graph, basis_indexes)
        print('Not basis:', not_basis_edges)

        delta = get_delta(costs, u, not_basis_edges)
        print('Estimate vector:', delta)

        bad = get_bad_edge(costs, u, not_basis_edges)
        if not bad:
            return x, basis_indexes

        print('Bad is:', bad)

        straight, reverse = get_cycle(basis_indexes, bad[1], bad[0])
        print('Straight', straight)
        print('Reverse', reverse)

        min_x, min_pair = min_cost_edge(reverse)

        for from_, to_ in straight:
            for i in range(len(x[from_])):
                if x[from_][i][0] == to_:
                    x[from_][i] = (x[from_][i][0],
                                  x[from_][i][1] + min_x)

        for r in reverse:
            for i in range(len(x[r[0]])):
                if x[r[0]][i][0] == r[1]:
                    x[r[0]][i] = (x[r[0]][i][0],
                                  x[r[0]][i][1] - min_x)

        basis_indexes.remove(min_pair)
        basis_indexes.append(bad)


def get_data():
    data = [
        [(1, 1)],
        [(5, 3)],
        [(1, 3), (3, 5)],
        [],
        [(2, 4), (3, 1)],
        [(0, -2), (2, 3), (4, 4)]
    ]
    basis = [
        (0, 1),
        (2, 1),
        (5, 2),
        (2, 3),
        (4, 3)
    ]
    x = [
        [(1, 1)],
        [(5, 0)],
        [(1, 3), (3, 1)],
        [],
        [(2, 0), (3, 5)],
        [(0, 0), (2, 9), (4, 0)]
    ]
    return data, basis, x


def get_sample():
    data = [
        [(1, 9), (7, 5)],
        [(2, 1), (5, 3), (6, 5)],
        [(8, -2)],
        [(2, -3)],
        [(3, 6)],
        [(4, 8)],
        [(2, -1), (3, 4), (4, 7), (8, 1)],
        [(6, 2), (8, 2)],
        [(5, 6)]
    ]
    basis = [
        (0, 1),
        (0, 7),
        (1, 6),
        (1, 2),
        (6, 4),
        (4, 3),
        (5, 4),
        (8, 5)
    ]
    x = [
        [(1, 2), (7, 7)],
        [(2, 4), (5, 0), (6, 3)],
        [(8, 0)],
        [(2, 0)],
        [(3, 3)],
        [(4, 4)],
        [(2, 0), (3, 0), (4, 5), (8, 0)],
        [(6, 0), (8, 0)],
        [(5, 2)]
    ]
    return data, basis, x


data, basis_indexes, x = get_data()
answer = run(data, basis_indexes, x)
if answer is not None:
    print('Answer. X: {}'.format(answer[0]))
    x = answer[0]
    d = data
    s = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            s += x[i][j][1] * get_c(d, i, x[i][j][0])
    print('S:', s)
