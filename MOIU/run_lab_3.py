import numpy as np
import lab_3.lib as lib


def test1():
    A = np.array([
        [1, 1, 1],
        [2, 2, 2],
        [3, 3, 3]])
    b = [0, 0, 0]

    lib.start_phase(A, b)


def test2():
    A = np.array([
        [0.0, 1.0, 4.0, 1.0, 0.0, -8.0, 1.0, 5.0],
        [0.0, -1.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 2.0, -1.0, 0.0, -1.0, 3.0, -1.0, 0.0],
        [1.0, 1.0, 1.0, 1.0, 0.0, 3.0, 1.0, 1.0]
    ])
    b = [36.0, -11.0, 10.0, 20.0]

    lib.start_phase(A, b)


def main():
    test1()
    input()

    test2()


if __name__ == '__main__':
    main()
