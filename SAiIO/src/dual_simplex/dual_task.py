import numpy as np


class DualTask:
    def __init__(self, A, b, c, d_lo, d_hi):
        self.A = np.array(A)
        self.b = b
        self.c = c
        self.d_lo = np.array(d_lo)
        self.d_hi = np.array(d_hi)
        self.n, self.m = self.A.shape