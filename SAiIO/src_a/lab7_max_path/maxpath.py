import numpy as np


def build_graph(pairs):
    n = max(map(lambda p: max(p[0], p[1]), pairs))
    G = [[] for _ in range(n)]
    for from_, to, weight in pairs:
        G[from_ - 1].append(to - 1)
    return G[:n], n


def build_parents_graph(pairs):
    n = max(map(lambda p: max(p[0], p[1]), pairs))
    G = [[] for _ in range(n)]
    for from_, to, weight in pairs:
        G[to - 1].append((from_ - 1, weight))
    return G


def get_step_vertices(g, parents, I):
    w = set()
    for v in I:
        for dest in g[v]:
            if dest not in I:
                w.add(dest)
    
    for v in w:
        if set(map(lambda x: x[0], parents[v])).issubset(I):
            yield v


def restore_path(f, dest):
    path = []
    while f[dest] != -1:
        dest = f[dest]
        path.append(dest)
    
    return path


def solve(pairs, src, dest):
    src -= 1
    dest -= 1
    g, n = build_graph(pairs)
    parents = build_parents_graph(pairs)

    B = [0] * n
    f = [-1] * n
    I = set({src})

    while True:
        # находим все смежные с множеством вершины,
        # все входящие ребра в которые исходят из вершины из I
        w = list(get_step_vertices(g, parents, I))

        if len(w) == 0: break

        for v in w:
            for parent, weight in parents[v]:
                if B[v] < B[parent] + weight:
                    B[v] = B[parent] + weight
                    f[v] = parent
            I.add(v)

    return B[dest], restore_path(f, dest)
