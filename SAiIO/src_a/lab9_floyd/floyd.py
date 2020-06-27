import numpy as np
from pprint import pprint

def solve(g):
    n = len(g)
    d = g
    r, _ = np.meshgrid(range(n), range(n))

    for j in range(1, n):
        for i in range(n):
            for k in range(n):
                if d[i][k] > d[i][j - 1] + d[j - 1][k]:
                    d[i][k] = d[i][j - 1] + d[j - 1][k]
                    r[i][k] = j - 1

    r = list(map(list, r))
    return d, r