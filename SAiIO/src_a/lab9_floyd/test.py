import unittest
import floyd
import numpy as np


class FloydTestCase(unittest.TestCase):
    def test_task1(self):
        i = np.inf
        g = [[0, 9, i, 3, i, i, i, i],
             [9, 0, 2, i, 7, i, i, i],
             [i, 2, 0, 2, 4, 8, 6, i],
             [3, i, 2, 0, i, i, 5, i],
             [i, 7, 4, i, 0, 10, i, i],
             [i, i, 8, i, 10, 0, 7, i],
             [i, i, 6, 5, i, 7, 0, i],
             [i, i, i, i, 9, 12, 10, 0]]
        d, r = floyd.solve(g)

        self.assertListEqual(d, [[0, 7, 5, 3, 9, 13, 8, i],
                                 [7, 0, 2, 4, 6, 10, 8, i],
                                 [5, 2, 0, 2, 4, 8, 6, i],
                                 [3, 4, 2, 0, 6, 10, 5, i],
                                 [9, 6, 4, 6, 0, 10, 10, i],
                                 [13, 10, 8, 10, 10, 0, 7, i],
                                 [8, 8, 6, 5, 10, 7, 0, i],
                                 [18, 15, 13, 15, 9, 12, 10, 0]])

        self.assertListEqual(r, [[0, 3, 3, 3, 3, 3, 3, 7],
                                 [3, 1, 2, 2, 2, 2, 2, 7],
                                 [3, 1, 2, 3, 4, 5, 6, 7],
                                 [0, 2, 2, 3, 2, 2, 6, 7],
                                 [3, 2, 2, 2, 4, 5, 2, 7],
                                 [3, 2, 2, 2, 4, 5, 6, 7],
                                 [3, 2, 2, 3, 2, 5, 6, 7],
                                 [4, 4, 4, 4, 4, 5, 6, 7]])
    
    def test_task2(self):
        i = np.inf
        g = [[0, 3, 2, 6, i, i, i, i, i],
             [i, 0, i, 2, i, i, i, i, i],
             [i, i, 0, i, i, 4, i, i, i],
             [i, i, 3, 0, 1, i, 6, i, i],
             [i, i, i, i, 0, i, 7, 5, i],
             [i, i, i, i, 5, 0, i, 4, i],
             [i, i, i, i, i, i, 0, 2, 4],
             [i, i, i, i, i, i, i, 0, 4],
             [i, i, i, i, i, i, i, i, 0]]
        d, r = floyd.solve(g)

        self.assertListEqual(d, [[0, 3, 2, 5, 6, 6, 11, 10, 14],
                                 [i, 0, 5, 2, 3, 9, 8, 8, 12],
                                 [i, i, 0, i, 9, 4, 16, 8, 12],
                                 [i, i, 3, 0, 1, 7, 6, 6, 10],
                                 [i, i, i, i, 0, i, 7, 5, 9],
                                 [i, i, i, i, 5, 0, 12, 4, 8],
                                 [i, i, i, i, i, i, 0, 2, 4],
                                 [i, i, i, i, i, i, i, 0, 4],
                                 [i, i, i, i, i, i, i, i, 0]])



if __name__ == "__main__":
    unittest.main()
