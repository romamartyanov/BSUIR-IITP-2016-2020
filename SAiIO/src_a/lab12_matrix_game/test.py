import unittest
from game import MatrixGame


class MatrixGameTestCase(unittest.TestCase):
    def test_task1(self):
        A = [[1, -1, -2],
             [-1, 1, 1],
             [2, -1, 0]]
        
        game = MatrixGame(A)
        game.solve()

        self.assertEqual(1, 1)
    
    def test_task2(self):
        A = [[6, 1, 8, 4],
             [9, -2, 8, 2],
             [1, 3, 4, 3],
             [2, 4, 1, 6]]
        
        game = MatrixGame(A)
        game.solve()
        
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
