import unittest
from dual import DualSimplex, NoPlanException


class SimplexTest(unittest.TestCase):
    def test_should_solve_task1(self):
        A = [[2, 1, -1, 0, 0, 1],
             [1, 0, 1, 1, 0, 0],
             [0, 1, 0, 0, 1, 0]]
        b = [2, 5, 0]
        c = [3, 2, 0, 3, -2, -4]
        d_lo = [0, -1, 2, 1, -1, 0]
        d_hi = [2, 4, 4, 3, 3, 5]

        dual = DualSimplex(A, b, c, d_lo, d_hi)
        x, J, f_val = dual.solve([3, 4, 5])

        x_expected = [3 / 2, 1, 2, 3 / 2, -1, 0]
        for i, xi in enumerate(x):
            self.assertAlmostEqual(xi, x_expected[i], 3)
        self.assertAlmostEqual(f_val, 13, 5)

    def test_should_solve_task2(self):
        A = [[1, -5, 3, 1, 0, 0],
             [4, -1, 1, 0, 1, 0],
             [2, 4, 2, 0, 0, 1]]
        b = [-7, 22, 30]
        c = [7, -2, 6, 0, 5, 2]
        d_lo = [2, 1, 0, 0, 1, 1]
        d_hi = [6, 6, 5, 2, 4, 6]

        dual = DualSimplex(A, b, c, d_lo, d_hi)
        x, J, f_val = dual.solve()

        x_expected = [5, 3, 1, 0, 4, 6]
        for i, xi in enumerate(x):
            self.assertAlmostEqual(xi, x_expected[i], 5)
        self.assertAlmostEqual(f_val, 67, 5)

    def test_should_solve_task3(self):
        A = [[1, 0, 2, 2, -3, 3],
             [0, 1, 0, -1, 0, 1],
             [1, 0, 1, 3, 2, 1]]
        b = [15, 0, 13]
        c = [3, 0.5, 4, 4, 1, 5]
        d_lo = [0, 0, 0, 0, 0, 0]
        d_hi = [3, 5, 4, 3, 3, 4]

        dual = DualSimplex(A, b, c, d_lo, d_hi)
        x, J, f_val = dual.solve()

        x_expected = [3, 0, 4, 1.1818, 0.6364, 1.1818]
        for i, xi in enumerate(x):
            self.assertAlmostEqual(xi, x_expected[i], 4)
        self.assertAlmostEqual(f_val, 36.2727, 4)

    def test_should_solve_task4(self):
        A = [[1, 0, 0, 12, 1, -3, 4, -1],
             [0, 1, 0, 11, 12, 3, 5, 3],
             [0, 0, 1, 1, 0, 22, -2, 1]]
        b = [40, 107, 61]
        c = [2, 1, -2, -1, 4, -5, 5, 5]
        d_lo = [0, 0, 0, 0, 0, 0, 0, 0]
        d_hi = [3, 5, 5, 3, 4, 5, 6, 3]

        dual = DualSimplex(A, b, c, d_lo, d_hi)
        x, J, f_val = dual.solve()

        x_expected = [3, 5, 0, 1.8779, 2.7545, 3.0965, 6, 3]
        for i, xi in enumerate(x):
            self.assertAlmostEqual(xi, x_expected[i], 4)
        self.assertAlmostEqual(f_val, 49.6577, 4)

    def test_should_solve_task5(self):
        A = [[1, -3, 2, 0, 1, -1, 4, -1, 0],
             [1, -1, 6, 1, 0, -2, 2, 2, 0],
             [2, 2, -1, 1, 0, -3, 8, -1, 1],
             [4, 1, 0, 0, 1, -1, 0, -1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1]]
        b = [3, 9, 9, 5, 9]
        c = [-1, 5, -2, 4, 3, 1, 2, 8, 3]
        d_lo = [0] * 9
        d_hi = [5] * 9

        dual = DualSimplex(A, b, c, d_lo, d_hi)
        x, J, f_val = dual.solve()

        x_expected = [1.1579, 0.6942, 0, 0, 2.8797, 0, 1.0627, 3.2055, 0]
        for i, xi in enumerate(x):
            self.assertAlmostEqual(xi, x_expected[i], 4)
        self.assertAlmostEqual(f_val, 38.7218, 4)

    def test_should_solve_task6(self):
        A = [[1, 7, 2, 0, 1, -1, 4],
             [0, 5, 6, 1, 0, -3, -2],
             [3, 2, 2, 1, 1, 1, 5]]
        b = [1, 4, 7]
        c = [1, 2, 1, -3, 3, 1, 0]
        d_lo = [-1, 1, -2, 0, 1, 2, 4]
        d_hi = [3, 2, 2, 5, 3, 4, 5]

        dual = DualSimplex(A, b, c, d_lo, d_hi)
        self.assertRaises(NoPlanException, dual.solve)
    
    def test_should_solve_task7(self):
        A = [[2, -1, 1, 0, 0, -1, 3],
             [0, 4, -1, 2, 3, -2, 2],
             [3, 1, 0, 1, 0, 1, 4]]
        b = [1.5, 9, 2]
        c = [0, 1, 2, 1, -3, 4, 7]
        d_lo = [0, 0, -3, 0, -1, 1, 0]
        d_hi = [3, 3, 4, 7, 5, 3, 2]

        dual = DualSimplex(A, b, c, d_lo, d_hi)
        x, J, f_val = dual.solve()

        x_expected = [0, 1, 3.5, 0, 3.5, 1, 0]
        for i, xi in enumerate(x):
            self.assertAlmostEqual(xi, x_expected[i], 4)
        self.assertAlmostEqual(f_val, 1.5, 4)

    def test_should_solve_task8(self):
        A = [[2, 1, 0, 3, -1, -1],
             [0, 1, -2, 1, 0, 3],
             [3, 0, 1, 1, 1, 1]]
        b = [2, 2, 5]
        c = [0, -1, 1, 0, 4, 3]
        d_lo = [2, 0, -1, -3, 2, 1]
        d_hi = [7, 3, 2, 3, 4, 5]

        dual = DualSimplex(A, b, c, d_lo, d_hi)

        self.assertRaises(NoPlanException, dual.solve)
    
    def test_should_solve_task9(self):
        A = [[1, 3, 1, -1, 0, -3, 2, 1],
             [2, 1, 3, -1, 1, 4, 1, 1],
             [-1, 0, 2, -2, 2, 1, 1, 1]]
        b = [4, 12, 4]
        c = [2, -1, 2, 3, -2, 3, 4, 1]
        d_lo = [-1] * 8
        d_hi = [2, 3, 1, 4, 3, 2, 4, 4]

        dual = DualSimplex(A, b, c, d_lo, d_hi)
        x, J, f_val = dual.solve()

        x_expected = [-1, 0.4074, 1, 4, -0.3704, 1.7407, 4, 4]
        for i, xi in enumerate(x):
            self.assertAlmostEqual(xi, x_expected[i], 4)
        self.assertAlmostEqual(f_val, 37.5556, 4)

if __name__ == "__main__":
    unittest.main()
