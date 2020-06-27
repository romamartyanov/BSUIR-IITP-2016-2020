from dual_task import DualTask
from gomor import Gomor
import unittest
import numpy as np

class GomorTestCase(unittest.TestCase):
    def test_task1(self):
        A = [[1, -5, 3, 1, 0, 0],
             [4, -1, 1, 0, 1, 0],
             [2, 4, 2, 0, 0, 1]]
        b = [-8, 22, 30]
        c = [7, -2, 6, 0, 5, 2]
        d_lo = [0] * 6
        d_hi = [1e9] * 6

        task = DualTask(A, b, c, d_lo, d_hi)
        gomor = Gomor(task)
        x, J, f = gomor.solve()

        print(x)
        x_exp = [0, 2, 0, 2, 24, 22]
        for i in range(len(x)):
            self.assertAlmostEqual(x[i], x_exp[i], 2)
        self.assertAlmostEqual(f, 160)
    
    def test_task2(self):
        A = [[1, -3, 2, 0, 1, -1, 4, -1, 0],
             [1, -1, 6, 1, 0, -2, 2, 2, 0],
             [2, 2, -1, 1, 0, -3, 8, -1, 1],
             [4, 1, 0, 0, 1, -1, 0, -1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1]]
        b = [3, 9, 9, 5, 9]
        c = [-1, 5, -2, 4, 3, 1, 2, 8, 3]
        d_lo = [0] * 1000
        d_hi = [1e9] * 1000

        task = DualTask(A, b, c, d_lo, d_hi)
        gomor = Gomor(task)
        x, J, f = gomor.solve()

        print(x)
        x_exp = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        for i in range(len(x)):
            self.assertAlmostEqual(x[i], x_exp[i], 2)
        self.assertAlmostEqual(f, 23)
    
    def test_task3(self):
        A = [[1, 0, 0, 12, 1, -3, 4, -1],
             [0, 1, 0, 11, 12, 3, 5, 3],
             [0, 0, 1, 1, 0, 22, -2, 1]]
        b = [40, 107, 61]
        c = [2, 1, -2, -1, 4, -5, 5, 5]
        d_lo = [0] * 100
        d_hi = [1e9] * 100

        task = DualTask(A, b, c, d_lo, d_hi)
        gomor = Gomor(task)
        x, J, f = gomor.solve()

        print(x)
        x_exp = [77, 2, 5, 0, 0, 1, 0, 34]
        for i in range(len(x)):
            self.assertAlmostEqual(x[i], x_exp[i], 2)
        self.assertAlmostEqual(f, 311)
    
    def test_task4(self):
        A = [[1, 2, 3, 12, 1, -3, 4, -1, 2, 3],
             [0, 2, 0, 11, 12, 3, 5, 3, 4, 5],
             [0, 0, 2, 1, 0, 22, -2, 1, 6, 7]]
        b = [153, 123, 112]
        c = [2, 1, -2, -1, 4, -5, 5, 5, 1, 2]
        d_lo = [0] * 100
        d_hi = [1e9] * 100

        task = DualTask(A, b, c, d_lo, d_hi)
        gomor = Gomor(task)
        x, J, f = gomor.solve()

        print(x)
        x_exp = [188, 0, 4, 0, 0, 3, 0, 38, 0, 0]
        for i in range(len(x)):
            self.assertAlmostEqual(x[i], x_exp[i], 2)
        self.assertAlmostEqual(f, 543)
    
    def test_task5(self):
        A = [[2, 1, -1, -3, 4, 7],
             [0, 1, 1, 1, 2, 4],
             [6, -3, -2, 1, 1, 1]]
        b = [7, 16, 6]
        c = [1, 2, 1, -1, 2, 3]
        d_lo = [0] * 100
        d_hi = [1e9] * 100

        task = DualTask(A, b, c, d_lo, d_hi)
        gomor = Gomor(task)
        x, J, f = gomor.solve()

        print(x)
        x_exp = [5, 1, 11, 0, 0, 1]
        for i in range(len(x)):
            self.assertAlmostEqual(x[i], x_exp[i], 2)
        self.assertAlmostEqual(f, 21)

    def test_task6(self):
        A = [[0, 7, 1, -1, -4, 2, 4],
             [5, 1, 4, 3, -5, 2, 1],
             [2, 0, 3, 1, 0, 1, 5]]
        b = [12, 27, 19]
        c = [10, 2, 1, 7, 6, 3, 1]
        d_lo = [0] * 100
        d_hi = [1e9] * 100

        task = DualTask(A, b, c, d_lo, d_hi)
        gomor = Gomor(task)
        x, J, f = gomor.solve()

        print(x)
        x_exp = [5, 6, 0, 8, 6, 1, 0]
        for i in range(len(x)):
            self.assertAlmostEqual(x[i], x_exp[i], 2)
        self.assertAlmostEqual(f, 157)
    
    def test_task7(self):
        A = [[0, 7, -8, -1, 5, 2, 1],
             [3, 2, 1, -3, -1, 1, 0],
             [1, 5, 3, -1, -2, 1, 0],
             [1, 1, 1, 1, 1, 1, 1]]
        b = [6, 3, 7, 7]
        c = [2, 9, 3, 5, 1, 2, 4]
        d_lo = [0] * 100
        d_hi = [1e9] * 100

        task = DualTask(A, b, c, d_lo, d_hi)
        gomor = Gomor(task)
        x, J, f = gomor.solve()

        print(x)
        x_exp = [1, 1, 1, 1, 1, 1, 1]
        for i in range(len(x)):
            self.assertAlmostEqual(x[i], x_exp[i], 2)
        self.assertAlmostEqual(f, 26)
    
    def test_task8(self):
        A = [[1, 0, -1, 3, -2, 0, 1],
             [0, 2, 1, -1, 0, 3, -1],
             [1, 2, 1, 4, 2, 1, 1]]
        b = [4, 8, 24]
        c = [-1, -3, -7, 0, -4, 0, -1]
        d_lo = [0] * 100
        d_hi = [1e9] * 100

        task = DualTask(A, b, c, d_lo, d_hi)
        gomor = Gomor(task)
        x, J, f = gomor.solve()

        print(x)
        x_exp = [1, 1, 0, 3, 3, 3, 0]
        for i in range(len(x)):
            self.assertAlmostEqual(x[i], x_exp[i], 2)
        self.assertAlmostEqual(f, -16)
    
    def test_task9(self):
        A = [[1, -3, 2, 0, 1, -1, 4, -1, 0],
             [1, -1, 6, 1, 0, -2, 2, 2, 0],
             [2, 2, -1, 1, 0, -3, 2, -1, 1],
             [4, 1, 0, 0, 1, -1, 0, -1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1]]
        b = [3, 9, 9, 5, 9]
        c = [-1, 5, -2, 4, 3, 1, 2, 8, 3]
        d_lo = [0] * 100
        d_hi = [1e9] * 100

        task = DualTask(A, b, c, d_lo, d_hi)
        gomor = Gomor(task)
        x, J, f = gomor.solve()

        print(x)
        x_exp = [0, 1, 1, 2, 0, 0, 1, 0, 4]
        for i in range(len(x)):
            self.assertAlmostEqual(x[i], x_exp[i], 2)
        self.assertAlmostEqual(f, 25)

if __name__ == "__main__":
    unittest.main()
