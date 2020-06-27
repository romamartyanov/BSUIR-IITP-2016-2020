import numpy as np
import unittest
from maxpath import solve

class MaxPathTestCase(unittest.TestCase):
    def test_task1(self):
        pairs = [(1, 2, 2), (1, 6, 1), (2, 3, 2), (6, 2, 4), 
                 (6, 3, 4), (6, 5, 1), (2, 5, 7), (5, 3, 1), 
                 (3, 4, 8), (5, 4, 1)]
        b, f = solve(pairs, src=1, dest=4)
        
        self.assertEqual(21, b)
        self.assertListEqual([2, 4, 1, 5, 0], f)
    
    def test_task2(self):
        pairs = [(1, 2, 5), (1, 3, 6), (1, 4, 4), (1, 5, 1), 
                 (2, 3, 4), (2, 5, 2), (2, 4, 3), (3, 5, 5), 
                 (3, 7, 3), (4, 6, 4), (4, 8, 3), (4, 7, 7),
                 (5, 8, 4), (6, 7, 2), (6, 8, 5), (7, 5, 2),
                 (7, 8, 1)]
        b, f = solve(pairs, src=1, dest=8)
  
        self.assertEqual(21, b)
    
    def test_task3(self):
        pairs = [(1, 2, 3), (1, 6, 3), (1, 3, 4), (1, 5, 5), 
                 (2, 5, 2), (3, 2, 1), (3, 5, 6), (3, 7, 3), 
                 (5, 6, 4), (5, 7, 1), (5, 8, 4), (6, 7, 2),
                 (6, 8, 5), (7, 8, 1)]
        b, f = solve(pairs, src=1, dest=8)
  
        self.assertEqual(19, b)


if __name__ == "__main__":
    unittest.main()
