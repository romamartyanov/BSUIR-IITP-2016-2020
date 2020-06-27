import numpy as np


class DualTask:
    def __init__(self, A: list, b: list, c: list, d_lo: list, d_hi: list):
        self.A: np.array = np.array(A)
        self.b: list = b
        self.c: list = c
        self.d_lo: np.array = np.array(d_lo)
        self.d_hi: np.array = np.array(d_hi)
        self.m, self.n = self.A.shape
    
    def remove(self, row, col):
        self.A = np.delete(self.A, row, axis=0)
        self.A = np.delete(self.A, col, axis=1)

        del self.b[row]
        del self.c[col]

        self.d_lo = np.delete(self.d_lo, col)
        self.d_hi = np.delete(self.d_hi, col)

        self.n -= 1
        self.m -= 1

    def extend(self, a, b, J):
        J_not_base = [j for j in range(self.n) if j not in J]

        restriction = np.zeros(self.n)
        restriction[J_not_base] = -a[J_not_base]

        self.n += 1
        self.m += 1
        
        self.A = np.vstack((self.A, restriction))
        self.A = np.hstack((self.A, np.zeros((self.m, 1))))
        self.A[-1, -1] = 1

        self.b.append(-b)
        self.c.append(0)

        self.d_lo = np.append(self.d_lo, 0)
        self.d_hi = np.append(self.d_hi, 1e9)

