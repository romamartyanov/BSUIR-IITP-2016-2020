import unittest

from src.max_path import MaxPath


class MaxPathTestCase(unittest.TestCase):
    def test_1(self):
        graph = [((1, 2), 2), ((1, 6), 1), ((2, 3), 2), ((6, 2), 4), ((6, 3), 4),
                 ((6, 5), 1), ((2, 5), 7), ((5, 3), 1), ((3, 4), 8), ((5, 4), 1)]

        max_path = MaxPath(graph, 1, 4, 6)
        b, f = max_path.find_max_path()
        self.assertEqual(21, b)
        self.assertListEqual([2, 4, 1, 5, 0], f)

    def test_2(self):
        graph = [((1, 2), 5), ((1, 3), 6), ((1, 4), 4), ((1, 5), 1), ((2, 3), 4),
                 ((2, 5), 2), ((2, 4), 3), ((3, 5), 5), ((3, 7), 3), ((4, 6), 4),
                 ((4, 8), 3), ((4, 7), 7), ((5, 8), 4), ((6, 7), 2), ((6, 8), 5),
                 ((7, 5), 2), ((7, 8), 1)]

        max_path = MaxPath(graph, 1, 8, 8)
        b, f = max_path.find_max_path()
        self.assertEqual(21, b)

    def test_3(self):
        graph = [((1, 2), 3), ((1, 6), 3), ((1, 3), 4), ((1, 5), 5), ((2, 5), 2),
                 ((3, 2), 1), ((3, 5), 6), ((3, 7), 3), ((5, 6), 4), ((5, 7), 1),
                 ((5, 8), 4), ((6, 7), 2), ((6, 8), 5), ((7, 8), 1)]

        max_path = MaxPath(graph, 1, 8, 8)
        b, f = max_path.find_max_path()
        self.assertEqual(19, b)


if __name__ == "__main__":
    unittest.main()
