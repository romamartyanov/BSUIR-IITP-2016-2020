import numpy as np
import math


def Rotation(m, eps):
    n = m.shape[0]
    vector = np.eye(m.shape[0])

    A = m.copy()
    iterations = 0

    while True:
        n = A.shape[0]

        max_element = 0
        max_i = 0
        max_j = 0

        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i][j]) > max_element:
                    max_element = abs(A[i][j])
                    max_i = i
                    max_j = j

        if max_element <= eps:
            break

        fi = 0.5 * math.atan(2.0 * max_element / (A[max_i][max_i] - A[max_j][max_j]))

        U = np.eye(n)
        U[max_i][max_i] = math.cos(fi)
        U[max_j][max_j] = math.cos(fi)
        U[max_i][max_j] = -math.sin(fi)
        U[max_j][max_i] = math.sin(fi)

        vector = np.dot(vector, U)
        iterations += 1

        A = np.dot(np.dot(U.T, A), U)
        print('max_elm:', max_element, 'i: ', max_i, 'j: ', max_j)
        print('sin(fi): ', math.sin(fi))
        print('cos(fi): ', math.cos(fi))
        print('a:\n', A)

    print("Количество итераций: ", iterations)
    return A, vector


def main():
    a = np.array([[3.389, 0.273, 0.126, 0.418],
                  [0.329, 2.796, 0.179, 0.278],
                  [0.186, 0.275, 2.987, 0.316],
                  [0.197, 0.219, 0.274, 3.127]])

    a = np.dot(a.T, a)
    print('a:\n', a, '\n')

    a, vector = Rotation(a, 1)

    print(a)
    print()
    print("Собственные значения:\n", [a[i][i] for i in range(len(a))])
    print()
    print("Собственные векторы:\n", vector)
    print()


if __name__ == "__main__":
    main()
