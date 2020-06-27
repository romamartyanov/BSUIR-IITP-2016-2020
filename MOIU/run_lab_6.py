import numpy as np

from lab_6.lib import quadratic_programming_problem


def test_1():
    A = np.array([
        [1, 2, 0, 1, 0, 4, -1, -3],
        [1, 3, 0, 0, 1, -1, -1, 2],
        [1, 4, 1, 0, 0, 2, -2, 0]
    ])
    b = np.array([4, 5, 6])
    B = np.array([
        [1, 1, -1, 0, 3, 4, -2, 1],
        [2, 6, 0, 0, 1, -5, 0, -1],
        [-1, 2, 0, 0, -1, 1, 1, 1]
    ])
    d = np.array([7, 3, 3])
    x = np.array([0, 0, 6, 4, 5, 0, 0, 0])
    J_op = np.array([3, 4, 5])
    J = np.array([3, 4, 5])

    quadratic_programming_problem(A, d, x, J_op, J, B, True)


def test_2():
    A = np.array([
        [11, 0, 0, 1, 0, -4, -1, 1],
        [1, 1, 0, 0, 1, -1, -1, 1],
        [1, 1, 1, 0, 1, 2, -2, 1]
    ])

    B = np.array([
        [1, -1, 0, 3, -1, 5, -2, 1],
        [2, 5, 0, 0, -1, 4, 0, 0],
        [-1, 3, 0, 5, 4, -1, -2, 1]
    ])
    d = np.array([6, 10, 9])
    x = np.array([0.7273, 1.2727, 3, 0, 0, 0, 0, 0])
    J_op = np.array([1, 2, 3])
    J = np.array([1, 2, 3])

    quadratic_programming_problem(A, d, x, J_op, J, B, True)


if __name__ == "__main__":
    test_1()
    input()

    test_2()
