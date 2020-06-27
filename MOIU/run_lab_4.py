from numpy import array

from lab_4.lib import double_simplex


def test_1_small():
    A = array([
        [-2, -1, -4, 1, 0],
        [-2, -2, -2, 0, 1]
    ])
    b = array([-1, -1.5])
    c = array([-4, -3, -7, 0, 0])
    J = array([4, 5])

    double_simplex(c, b, A, J)


def example_1():
    A = array([
        [-2, -1, 1, -7, 0, 0, 0, 2],
        [4, 2, 1, 0, 1, 5, -1, -5],
        [1, 1, 0, -1, 0, 3, -1, 1]
    ])
    b = array([-2, 4, 3])
    c = array([2, 2, 1, -10, 1, 4, -2, -3])
    J = array([2, 5, 7])

    double_simplex(c, b, A, J)


def test_3():
    A = array([
        [-2, -1, 1, -7, 0, 0, 0, 2],
        [-4, 2, 1, 0, 1, 5, -1, 5],
        [1, 1, 0, 1, 4, 3, 1, 1]
    ])
    b = array([-2, 8, -2])
    c = array([12, -2, -6, 20, -18, -5, -7, -20])
    J = array([2, 4, 6])

    double_simplex(c, b, A, J)


def test_4():
    A = array([
        [-2, -1, 10, -7, 1, 0, 0, 2],
        [-4, 2, 3, 0, 5, 1, -1, 0],
        [1, 1, 0, 1, -4, 3, -1, 1]
    ])
    b = array([-2, -5, 2])
    c = array([10, -2, -38, 16, -9, -9, -5, -7])
    J = array([2, 8, 5])

    double_simplex(c, b, A, J)


def main():
    test_1_small()
    input()

    example_1()
    input()

    test_3()
    input()

    test_4()


if __name__ == "__main__":
    main()
