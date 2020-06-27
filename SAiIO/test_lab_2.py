import unittest

from src.dual_simplex.bnb import BranchAndBound
from src.dual_simplex.dual_task import DualTask


class BranchAndBoundTest(unittest.TestCase):
    def test_task1(self):
        A = [[1, 0, 0, 12, 1, -3, 4, -1],
             [0, 1, 0, 11, 12, 3, 5, 3],
             [0, 0, 1, 1, 0, 22, -2, 1]]
        b = [40, 107, 61]
        c = [2, 1, -2, -1, 4, -5, 5, 5]
        d_lo = [0, 0, 0, 0, 0, 0, 0, 0]
        d_hi = [3, 5, 5, 3, 4, 5, 6, 3]

        task = DualTask(A, b, c, d_lo, d_hi)
        dual = BranchAndBound(task)
        dual.solve()

        x_expected = [1, 1, 2, 2, 3, 3, 6, 3]
        for i, xi in enumerate(dual.x):
            self.assertAlmostEqual(xi, x_expected[i], 4)
        self.assertAlmostEqual(dual.mu, 39, 5)

    def test_task3(self):
        A = [[1, 0, 0, 12, 1, -3, 4, -1, 2.5, 3],
             [0, 1, 0, 11, 12, 3, 5, 3, 4, 5.1],
             [0, 0, 1, 1, 0, 22, -2, 1, 6.1, 7]]
        b = [43.5, 107.3, 106.3]
        c = [2, 1, -2, -1, 4, -5, 5, 5, 1, 2]
        d_lo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        d_hi = [2, 4, 5, 3, 4, 5, 4, 4, 5, 6]

        task = DualTask(A, b, c, d_lo, d_hi)
        dual = BranchAndBound(task)
        dual.solve()

        x_expected = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3]
        for i, xi in enumerate(dual.x):
            self.assertAlmostEqual(xi, x_expected[i], 4)
        self.assertAlmostEqual(dual.mu, 29, 5)

    def test_task4(self):
        A = [[4, 0, 0, 0, 0, -3, 4, -1, 2, 3],
             [0, 1, 0, 0, 0, 3, 5, 3, 4, 5],
             [0, 0, 1, 0, 0, 22, -2, 1, 6, 7],
             [0, 0, 0, 1, 0, 6, -2, 7, 5, 6],
             [0, 0, 0, 0, 1, 5, 5, 1, 6, 7]]
        b = [8, 5, 4, 7, 8]
        c = [2, 1, -2, -1, 4, -5, 5, 5, 1, 2]
        d_lo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        d_hi = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

        task = DualTask(A, b, c, d_lo, d_hi)
        dual = BranchAndBound(task)
        dual.solve()

        x_expected = [2, 5, 4, 7, 8, 0, 0, 0, 0, 0]
        for i, xi in enumerate(dual.x):
            self.assertAlmostEqual(xi, x_expected[i], 4)
        self.assertAlmostEqual(dual.mu, 26, 5)

    def test_task5(self):
        A = [[1, -5, 3, 1, 0, 0],
             [4, -1, 1, 0, 1, 0],
             [2, 4, 2, 0, 0, 1]]
        b = [-8, 22, 30]
        c = [7, -2, 6, 0, 5, 2]
        d_lo = [2, 1, 0, 0, 1, 1]
        d_hi = [6, 6, 5, 2, 4, 6]

        task = DualTask(A, b, c, d_lo, d_hi)
        dual = BranchAndBound(task)
        dual.solve()

        x_expected = [6, 3, 0, 1, 1, 6]
        for i, xi in enumerate(dual.x):
            self.assertAlmostEqual(xi, x_expected[i], 4)
        self.assertAlmostEqual(dual.mu, 53, 5)


if __name__ == "__main__":
    unittest.main()
