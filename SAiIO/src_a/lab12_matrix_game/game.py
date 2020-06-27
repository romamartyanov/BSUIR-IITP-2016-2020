import numpy as np
import scipy.optimize as sco


class MatrixGame:
    def __init__(self, A):
        self.A = np.array(A)
        self.n, self.m = self.A.shape
    
    def solve(self):
        A_ub = -np.copy(self.A).T
        b_ub = [0 for _ in range(self.m)]
        A_eq = [[1 for _ in range(self.n)] + [0]]
        b_eq = [1]

        ones_col = np.reshape([1 for _ in range(self.m)], (self.m, 1))
        A_ub = np.hstack((A_ub, ones_col))
        c = [0 for _ in range(self.n)] + [-1]

        print('A_eq: ')
        print('\t', A_eq)
        print('b_eq: ')
        print('\t', b_eq)
        print('\t', 'A_ub')
        print('\t', A_ub)
        print('\t', 'b_ub')
        print('\t', b_ub)
        print('\n\t', sco.linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq))


