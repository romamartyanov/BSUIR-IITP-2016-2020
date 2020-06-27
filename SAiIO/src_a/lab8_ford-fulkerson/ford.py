from pprint import pprint
import numpy as np


DIRECTION_FORWARD = 0
DIRECTION_BACKWARD = 1


def build_graph(pairs, to):
    G = {to: {}}
    for from_, to, weight in pairs:
        if from_ not in G:
            G[from_] = {}
        G[from_][to] = weight
    return G


def build_parents_graph(pairs, s):
    G = {s: {}}
    for from_, to, weight in pairs:
        if to not in G:
            G[to] = {}
        G[to][from_] = weight
    return G


def get_start_flow(g):
    g1 = {}

    for v, connections in g.items():
        g1[v] = {}
        for to, _ in connections.items():
            g1[v][to] = 0

    return g1


def find_alpha(s, t, cur_flow, g, g_forward):
    cur = t
    alpha = np.inf

    # минимальный увеличивающий поток
    while cur != s:
        prev, direction = g[cur]

        if direction == DIRECTION_FORWARD:
            allowed = g_forward[prev][cur] - cur_flow[prev][cur]
        else:
            allowed = cur_flow[cur][prev]

        alpha = min(alpha, allowed)
        cur = prev

    return alpha


def recalculate_path(s, t, cur_flow, g, alpha):
    cur = t
    # обновляем путь
    while cur != s:
        prev, direction = g[cur]

        if direction == DIRECTION_FORWARD:
            cur_flow[prev][cur] += alpha
        else:
            cur_flow[cur][prev] -= alpha

        cur = prev

    return cur_flow


def restore_flow(s, t, cur_flow, g, g_forward):
    alpha = find_alpha(s, t, cur_flow, g, g_forward)

    cur_flow = recalculate_path(s, t, cur_flow, g, alpha)

    return alpha, cur_flow


def ford(pairs, s, t):
    g_forward = build_graph(pairs, t)
    g_backward = build_parents_graph(pairs, s)

    cur_flow = get_start_flow(g_forward)

    flow = 0

    while True:
        # step 1 - инициализация
        ic = 1
        it = 1
        L = [s]
        g = {s: (0, DIRECTION_FORWARD)}
        p = {s: 1}
        p_inv = {1: s}
        i = s

        while True:
            # step 2 - обход всех исходящих непомеченных вершин
            for j, weight in g_forward[i].items():
                if j in L or cur_flow[i][j] >= weight:
                    continue

                g[j] = (i, DIRECTION_FORWARD)
                it += 1
                p[j] = it
                p_inv[it] = j

                L.append(j)

            # step 3 - обход всех входящих непомеченных вершин
            for j, weight in g_backward[i].items():
                if j in L or cur_flow[j][i] == 0:
                    continue

                g[j] = (i, DIRECTION_BACKWARD)
                it += 1
                p[j] = it
                p_inv[it] = j

                L.append(j)

            # step 4 - если дошли до стока
            if t in L:
                break

            # step 5 - переходим к следующей вершине
            ic += 1
            if ic not in p_inv:
                break

            i = p_inv[ic]

        # выходим, если не наашли увеличивающего пути
        if t not in g:
            return flow, cur_flow

        alpha, cur_flow = restore_flow(s, t, cur_flow, g, g_forward)

        flow += alpha

    return flow, cur_flow
