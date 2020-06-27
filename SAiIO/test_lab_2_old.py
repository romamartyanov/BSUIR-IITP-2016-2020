import unittest
from bnb import BranchAndBound
from dual_task import DualTask


class BranchAndBoundTestCase(unittest.TestCase):
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
    
    def test_task2(self):
        A = [[1, -3, 2, 0, 1, -1, 4, -1, 0],
             [1, -1, 6, 1, 0, -2, 2, 2, 0],
             [2, 2, -1, 1, 0, -3, 8, -1, 1],
             [4, 1, 0, 0, 1, -1, 0, -1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1]]
        b = [3, 9, 9, 5, 9]
        c = [-1, 5, -2, 4, 3, 1, 2, 8, 3]
        d_lo = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        d_hi = [5, 5, 5, 5, 5, 5, 5, 5, 5]

        task = DualTask(A, b, c, d_lo, d_hi)
        dual = BranchAndBound(task)
        dual.solve()

        x_expected = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        for i, xi in enumerate(dual.x):
            self.assertAlmostEqual(xi, x_expected[i], 4)
        self.assertAlmostEqual(dual.mu, 23, 5)
    
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
    
    def test_task6(self):
        A = [[1, 0, 0, 3, 1, -3, 4, -1],
             [0, 1, 0, 4, -3, 3, 5, 3],
             [0, 0, 1, 1, 0, 2, -2, 1]]
        b = [30, 78, 5]
        c = [2, 1, -2, -1, 4, -5, 5, 5]
        d_lo = [0, 0, 0, 0, 0, 0, 0, 0]
        d_hi = [5, 5, 3, 4, 5, 6, 6, 8]

        task = DualTask(A, b, c, d_lo, d_hi)
        dual = BranchAndBound(task)
        dual.solve()

        x_expected = [5, 5, 3, 4, 0, 1, 6, 8]
        for i, xi in enumerate(dual.x):
            self.assertAlmostEqual(xi, x_expected[i], 4)
        self.assertAlmostEqual(dual.mu, 70, 5)
    
    def test_task8(self):
        A = [[1, 0, 1, 0, 4, 3, 4],
             [0, 1, 2, 0, 55, 3.5, 5],
             [0, 0, 3, 1, 6, 2, -2.5]]
        b = [26, 185, 32.5]
        c = [1, 2, 3, -1, 4, -5, 6]
        d_lo = [0, 1, 0, 0, 0, 0, 0]
        d_hi = [1, 2, 5, 7, 8, 4, 2]

        task = DualTask(A, b, c, d_lo, d_hi)
        dual = BranchAndBound(task)
        dual.solve()

        x_expected = [1, 2, 3, 4, 3, 2, 1]
        for i, xi in enumerate(dual.x):
            self.assertAlmostEqual(xi, x_expected[i], 4)
        self.assertAlmostEqual(dual.mu, 18, 5)
    
    


if __name__ == "__main__":
    unittest.main()
