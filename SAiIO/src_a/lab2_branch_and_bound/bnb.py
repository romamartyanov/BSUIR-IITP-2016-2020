import numpy as np
import math

from dual_task import DualTask
from dual import DualSimplex

import random


def is_int(x):
    return abs(round(x) - x) < 0.001


def all_int(a):
    return all(is_int(x) for x in a)


def get_not_int(a):
    not_ints = []
    for i, x in enumerate(a):
        if not is_int(x):
            not_ints.append((i, x))

    return random.choice(not_ints)


class BranchAndBound:
    def __init__(self, initial_task):
        self.initial_task = initial_task

        self.iteration = 0
        self.queue = [initial_task]
        self.mu = 0
        self.x = None

    def __split_task(self, task, x):
        pos, x_val = get_not_int(x)
        #print('split by pos', pos, x_val)
        split_val = math.floor(x_val)

        task1 = DualTask(task.A, task.b, task.c, task.d_lo, task.d_hi)
        task1.d_hi[pos] = split_val

        task2 = DualTask(task.A, task.b, task.c, task.d_lo, task.d_hi)
        task2.d_lo[pos] = split_val + 1

        return task1, task2

    def solve(self):
        #print('\n==================================')
        
        if self.iteration == 10000:
            raise Exception("Достигнут лимит итераций")
        
        if len(self.queue) == 0:
            return

        task = self.queue.pop(0)
        dual = DualSimplex(task)

        #print('Solving task: ')
        #print(task.d_lo)
        #print(task.d_hi)

        try:
            x, _, f_val = dual.solve()
            x = np.around(x, decimals=4)
        except Exception as e:
            #print(e)
            return

        if f_val < self.mu:
            return

        if all_int(x):
            if self.mu < f_val:
                self.mu = f_val
                self.x = x
            return
        
        task1, task2 = self.__split_task(task, x)

        #print(x)
        #print('-----')

        self.queue.append(task1)
        self.queue.append(task2)
        self.solve()
        self.solve()
