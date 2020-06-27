import numpy as np


class Floyd:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)

    def solve(self):
        d = self.graph
        R = [[i for i in range(self.n)] for _ in range(self.n)]

        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if d[i][j] > d[i][k] + d[k][j]:
                        R[i][j] = k

                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

        return d, R
