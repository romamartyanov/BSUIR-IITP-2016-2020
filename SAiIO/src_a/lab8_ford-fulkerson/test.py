import unittest
from ford import ford


class FordFulkersonTestCase(unittest.TestCase):
    def test_task1(self):
        pairs = [
            [0, 1, 4], [0, 3, 9], [1, 3, 2],
            [1, 4, 4], [3, 2, 1], [3, 5, 6],
            [2, 4, 1], [2, 5, 10], [4, 5, 1],
            [4, 6, 2], [5, 6, 9]
        ]
        s = 0
        t = 6
        flow, _ = ford(pairs, s, t)

        self.assertEqual(flow, 10)
    
    def test_task2(self):
        pairs = [
            [0, 1, 3], [0, 2, 2], [0, 3, 1], [0, 5, 6],
            [1, 3, 1], [1, 4, 2], 
            [2, 4, 2], [2, 3, 1], [2, 5, 4],
            [3, 5, 5], [3, 4, 7], [3, 6, 4], [3, 7, 1],
            [4, 6, 3], [4, 7, 2],
            [5, 7, 4],
            [6, 5, 3], [6, 7, 5]
        ]
        s = 0
        t = 7
        flow, _ = ford(pairs, s, t)

        self.assertEqual(flow, 10)

    def test_task3(self):
        pairs = [
            [0, 1, 4], [0, 2, 1], [0, 4, 1], [0, 5, 5], [0, 6, 2],
            [1, 3, 1], [1, 5, 6], 
            [2, 4, 2],
            [3, 2, 6], [3, 6, 3],
            [4, 5, 4], [4, 7, 3],
            [5, 7, 3], [5, 6, 1], [5, 8, 6],
            [6, 7, 4], [6, 8, 5],
            [7, 8, 4]
        ]
        s = 0
        t = 8
        flow, _ = ford(pairs, s, t)

        self.assertEqual(flow, 13)
    
    def test_task4(self):
        pairs = [
            [0, 1, 2], [0, 2, 1], [0, 4, 2],
            [1, 3, 2], [1, 4, 1], 
            [2, 4, 3], [2, 5, 2],
            [3, 6, 1], [3, 7, 2],
            [4, 5, 1], [4, 6, 4], [4, 7, 3], [4, 8, 3],
            [5, 7, 2], [5, 8, 2],
            [6, 7, 5], [6, 9, 3],
            [7, 8, 1], [7, 9, 4],
            [8, 9, 3]
        ]
        s = 0
        t = 9
        flow, _ = ford(pairs, s, t)

        self.assertEqual(flow, 5)

    def test_task5(self):
        pairs = [
            [0, 1, 3], [0, 2, 6], [0, 3, 3], [0, 4, 2],
            [1, 2, 4], [1, 3, 1], [1, 4, 4], 
            [2, 6, 3], [2, 7, 2],
            [3, 2, 1], [3, 4, 5], [3, 6, 1], [3, 7, 2],
            [4, 5, 1],
            [5, 3, 3], [5, 6, 1],
            [6, 7, 4]
        ]
        s = 0
        t = 7
        flow, _ = ford(pairs, s, t)

        self.assertEqual(flow, 8)


if __name__ == "__main__":
    unittest.main()
