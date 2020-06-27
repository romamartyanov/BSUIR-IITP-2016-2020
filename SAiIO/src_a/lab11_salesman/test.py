import unittest
from salesman import HeldKarp


class SalesmanTestCase(unittest.TestCase):
    def test_task1(self):
        dists = [[0,  2,  9, 10],
                 [1,  0,  6,  4],
                 [15, 7,  0,  8],
                 [6,  3, 12,  0]]
        
        karp = HeldKarp(dists)
        opt, path = karp.solve()

        self.assertEqual(opt, 21)
        self.assertListEqual(path, [0, 2, 3, 1])
