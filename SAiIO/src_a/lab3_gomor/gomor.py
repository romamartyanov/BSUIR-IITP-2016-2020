from dual_task import DualTask
from dual import DualSimplex
import numpy as np
import math
import random
import scipy.optimize as sco


def select_first_not_int(J, x):
    not_ints = []
    for i, j in enumerate(J):
        if not is_int(x[j]):
            not_ints.append(i)
    return random.choice(not_ints)


def is_int(x):
    return abs(round(x) - x) < 0.001


def all_int(a):
    return all(is_int(x) for x in a)


def fraction(x):
    if isinstance(x, float):
        return x - math.floor(x)
    
    return np.array([t - math.floor(t) for t in x])


class Gomor:
    def __init__(self, task: DualTask):
        self.task = task
        self.cur_task: DualTask = task

        self.J_art = []
        self.art_limitations = {}

    def exclude_artificial(self, x: list, J: list):
        J_copy = J[:]
        x_copy = x[:]

        col_ids = list(range(self.cur_task.n))
        row_ids = list(range(self.cur_task.m))

        for col in J:
            if col in self.J_art:
                row = self.art_limitations[col]
                
                for i in range(col + 1, len(col_ids)):
                    col_ids[i] -= 1
                
                for i in range(row + 1, len(row_ids)):
                    row_ids[i] -= 1

                J_copy.remove(col)
                self.cur_task.remove(row, col)
                self.J_art.remove(col)

                del self.art_limitations[col]
                x_copy = np.delete(x_copy, col_ids[col])
        
        self.J_art = [col_ids[val] for val in self.J_art]
        self.art_limitations = {col_ids[k]: row_ids[v] for k, v in self.art_limitations.items()}
        return list(x_copy), J_copy
    
    def remove_artificial(self, x: list):
        return np.delete(x, self.J_art)

    def solve(self, iteration=1):
        print('='*20)
        dual = DualSimplex(self.task)
        x, J, f = dual.solve()

        print('Before:')
        print('x:', x)
        print('J:', J)
        print('f:', f)
        x, J = self.exclude_artificial(x, J)
        print('After:')
        print('x:', x)
        print('J:', J)
        print('f:', f)

        if all_int(x):
            return self.remove_artificial(x), J, f

        jk = select_first_not_int(J, x)
        print('jk:', jk)

        print('A:')
        print(self.cur_task.A)
        print('A basic:')
        print(self.cur_task.A[:, J])
        inv_basis_row = np.linalg.inv(self.cur_task.A[:, J])[jk]
        b = fraction(np.dot(inv_basis_row, self.cur_task.b))
        a = fraction(np.dot(inv_basis_row, self.cur_task.A))

        print('a:', a)
        print('b:', b)

        self.cur_task.extend(a, b, J)
        self.J_art.append(self.cur_task.n - 1)
        self.art_limitations[self.cur_task.n - 1] = self.cur_task.m - 1

        return self.solve(iteration + 1)
