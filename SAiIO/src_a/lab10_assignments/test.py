import unittest
import numpy as np
from assignments import Assignments


class AssignmentTestCase(unittest.TestCase):
    def test_task1(self):
        costs = np.array([
            [2, -1, 9, 4],
            [3, 2, 5, 1],
            [13, 0, -3, 4],
            [5, 6, 1, 2]
        ])

        assignment = Assignments()
        ans, cost = assignment.solve(costs)

        self.assertEqual(cost, 1)
        self.assertListEqual(ans, [1, 0, 2, 3])

    def test_task2(self):
        costs = np.array([
            [6, 4, 13, 4, 19, 15, 11, 8],
            [17, 15, 18, 14, 0, 7, 18, 7],
            [3, 5, 11, 9, 7, 7, 18, 16],
            [17, 10, 16, 19, 9, 6, 1, 5],
            [14, 2, 10, 14, 11, 6, 4, 10],
            [17, 11, 17, 12, 1, 10, 6, 19],
            [13, 1, 4, 2, 2, 7, 2, 14],
            [12, 15, 19, 11, 13, 1, 7, 8]
        ])

        assignment = Assignments()
        ans, cost = assignment.solve(costs)

        self.assertEqual(cost, 23)
        self.assertListEqual(ans, [3, 7, 0, 6, 1, 4, 2, 5])

    def test_task3(self):
        costs = np.array([[5, 0, 7, 3],
                          [11, 0, 10, 4],
                          [0, 2, 3, 2],
                          [1, 3, 0, 5]])

        assignment = Assignments()
        _, _ = assignment.solve(costs)
