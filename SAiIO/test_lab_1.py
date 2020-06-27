import unittest

from src.dual_simplex.dual_task import DualTask
from src.dual_simplex.dual import DualSimplex

class DualSimplexTest(unittest.TestCase):
    def test_1(self):
        A = [[2, 1, -1, 0, 0, 1],
             [1, 0, 1, 1, 0, 0],
             [0, 1, 0, 0, 1, 0]]
        b = [2, 5, 0]
        c = [3, 2, 0, 3, -2, -4]
        d_lo = [0, -1, 2, 1, -1, 0]
        d_hi = [2, 4, 4, 3, 3, 5]

        task = DualTask(A, b, c, d_lo, d_hi)
        dual = DualSimplex(task)
        x, J, f_val = dual.solve([3, 4, 5])

        x_expected = [3 / 2, 1, 2, 3 / 2, -1, 0]
        for i, xi in enumerate(x):
            self.assertAlmostEqual(xi, x_expected[i], 3)
        self.assertAlmostEqual(f_val, 13, 5)

    def test_2(self):
        A = [[1, -5, 3, 1, 0, 0],
             [4, -1, 1, 0, 1, 0],
             [2, 4, 2, 0, 0, 1]]
        b = [-7, 22, 30]
        c = [7, -2, 6, 0, 5, 2]
        d_lo = [2, 1, 0, 0, 1, 1]
        d_hi = [6, 6, 5, 2, 4, 6]

        task = DualTask(A, b, c, d_lo, d_hi)
        dual = DualSimplex(task)
        x, J, f_val = dual.solve()

        x_expected = [5, 3, 1, 0, 4, 6]
        for i, xi in enumerate(x):
            self.assertAlmostEqual(xi, x_expected[i], 5)
        self.assertAlmostEqual(f_val, 67, 5)

    def test_3(self):
        A = [[1, 0, 2, 2, -3, 3],
             [0, 1, 0, -1, 0, 1],
             [1, 0, 1, 3, 2, 1]]
        b = [15, 0, 13]
        c = [3, 0.5, 4, 4, 1, 5]
        d_lo = [0, 0, 0, 0, 0, 0]
        d_hi = [3, 5, 4, 3, 3, 4]

        task = DualTask(A, b, c, d_lo, d_hi)
        dual = DualSimplex(task)
        x, J, f_val = dual.solve()

        x_expected = [3, 0, 4, 1.1818, 0.6364, 1.1818]
        for i, xi in enumerate(x):
            self.assertAlmostEqual(xi, x_expected[i], 4)
        self.assertAlmostEqual(f_val, 36.2727, 4)

    def test_4(self):
        A = [[1, 0, 0, 12, 1, -3, 4, -1],
             [0, 1, 0, 11, 12, 3, 5, 3],
             [0, 0, 1, 1, 0, 22, -2, 1]]
        b = [40, 107, 61]
        c = [2, 1, -2, -1, 4, -5, 5, 5]
        d_lo = [0, 0, 0, 0, 0, 0, 0, 0]
        d_hi = [3, 5, 5, 3, 4, 5, 6, 3]

        task = DualTask(A, b, c, d_lo, d_hi)
        dual = DualSimplex(task)
        x, J, f_val = dual.solve()

        x_expected = [3, 5, 0, 1.8779, 2.7545, 3.0965, 6, 3]
        for i, xi in enumerate(x):
            self.assertAlmostEqual(xi, x_expected[i], 4)
        self.assertAlmostEqual(f_val, 49.6577, 4)

if __name__ == "__main__":
    unittest.main()