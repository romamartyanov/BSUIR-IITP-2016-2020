import unittest

import numpy as np

from src.floyd import Floyd


class FloydTestCase(unittest.TestCase):
    def test_1(self):
        graph = [[0, 3, 2, 6, np.inf, np.inf, np.inf, np.inf, np.inf],
                 [np.inf, 0, np.inf, 2, np.inf, np.inf, np.inf, np.inf, np.inf],
                 [np.inf, np.inf, 0, np.inf, np.inf, 4, np.inf, np.inf, np.inf],
                 [np.inf, np.inf, 3, 0, 1, np.inf, 6, np.inf, np.inf],
                 [np.inf, np.inf, np.inf, np.inf, 0, np.inf, 7, 5, np.inf],
                 [np.inf, np.inf, np.inf, np.inf, 5, 0, np.inf, 4, np.inf],
                 [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0, 2, 4],
                 [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0, 4],
                 [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0]]

        floyd = Floyd(graph)
        d, r = floyd.solve()
        self.assertListEqual(
            d,
            [[0, 3, 2, 5, 6, 6, 11, 10, 14],
             [np.inf, 0, 5, 2, 3, 9, 8, 8, 12],
             [np.inf, np.inf, 0, np.inf, 9, 4, 16, 8, 12],
             [np.inf, np.inf, 3, 0, 1, 7, 6, 6, 10],
             [np.inf, np.inf, np.inf, np.inf, 0, np.inf, 7, 5, 9],
             [np.inf, np.inf, np.inf, np.inf, 5, 0, 12, 4, 8],
             [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0, 2, 4],
             [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0, 4],
             [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0]])

    def test_2(self):
        graph = [[0, 9, np.inf, 3, np.inf, np.inf, np.inf, np.inf],
                 [9, 0, 2, np.inf, 7, np.inf, np.inf, np.inf],
                 [np.inf, 2, 0, 2, 4, 8, 6, np.inf],
                 [3, np.inf, 2, 0, np.inf, np.inf, 5, np.inf],
                 [np.inf, 7, 4, np.inf, 0, 10, np.inf, np.inf],
                 [np.inf, np.inf, 8, np.inf, 10, 0, 7, np.inf],
                 [np.inf, np.inf, 6, 5, np.inf, 7, 0, np.inf],
                 [np.inf, np.inf, np.inf, np.inf, 9, 12, 10, 0]]

        floyd = Floyd(graph)
        d, r = floyd.solve()
        self.assertListEqual(
            d,
            [[0, 7, 5, 3, 9, 13, 8, np.inf],
             [7, 0, 2, 4, 6, 10, 8, np.inf],
             [5, 2, 0, 2, 4, 8, 6, np.inf],
             [3, 4, 2, 0, 6, 10, 5, np.inf],
             [9, 6, 4, 6, 0, 10, 10, np.inf],
             [13, 10, 8, 10, 10, 0, 7, np.inf],
             [8, 8, 6, 5, 10, 7, 0, np.inf],
             [18, 15, 13, 15, 9, 12, 10, 0]])
        self.assertListEqual(
            r,
            [[0, 3, 3, 3, 3, 3, 3, 7],
             [3, 1, 2, 2, 2, 2, 2, 7],
             [3, 1, 2, 3, 4, 5, 6, 7],
             [0, 2, 2, 3, 2, 2, 6, 7],
             [3, 2, 2, 2, 4, 5, 2, 7],
             [3, 2, 2, 2, 4, 5, 6, 7],
             [3, 2, 2, 3, 2, 5, 6, 7],
             [4, 4, 4, 4, 4, 5, 6, 7]])


if __name__ == "__main__":
    unittest.main()
