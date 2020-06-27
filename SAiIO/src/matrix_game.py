import numpy as np
import scipy.optimize as sco


class MatrixGame:
    def __init__(self, A):
        self.A = np.array(A)
        self.n, self.m = self.A.shape
    
    def solve(self):
        # Матрица ограничения неравенства.
        # Каждая строка A_ub определяет коэффициенты ограничения линейного неравенства по x.
        A_ub = -np.copy(self.A).T

        # Вектор ограничения неравенства.
        # Каждый элемент представляет верхнюю границу соответствующего значения A_ub @ x.
        b_ub = [0 for _ in range(self.m)]

        # Матрица ограничения равенства.
        # Каждая строка A_eq определяет коэффициенты ограничения линейного равенства по x.
        A_eq = [[1 for _ in range(self.n)] + [0]]

        # Вектор ограничения равенства.
        # Каждый элемент A_eq @ x должен равняться соответствующему элементу b_eq.
        b_eq = [1]

        ones_col = np.reshape([1 for _ in range(self.m)], (self.m, 1))
        A_ub = np.hstack((A_ub, ones_col))

        # Коэффициенты линейной целевой функции должны быть минимизированы.
        c = [0 for _ in range(self.n)] + [-1]

        print('A_eq: ')
        print('\t', A_eq)
        print('b_eq: ')
        print('\t', b_eq)
        print('A_ub')
        print('\t', A_ub)
        print('b_ub')
        print('\t', b_ub)

        # Линейное программирование: минимизировать линейную целевую функцию
        # с учетом ограничений линейного равенства и неравенства.
        print('\n', sco.linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq), '\n')


