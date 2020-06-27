#!/usr/bin/env python3 
import numpy as np


def symmetrize(A, b):
    return np.dot(A.T, A), np.dot(A.T, b)


def build_U(A):
    rows, cols = A.shape
    U = np.zeros((rows, cols))
    for i in range(rows):
        U[i][i] = np.sqrt(A[i][i] - np.sum([U[k][i] ** 2 for k in range(i)]))
        for j in range(i + 1, cols):
            U[i][j] = (A[i][j] - np.sum([U[k][i] * U[k][j] for k in range(i)])) / U[i][i]

        print(U)
    return U


def solve_sqrt(U, b):
    rows, cols = U.shape
    y = np.zeros(rows)
    UT = U.T
    for i in range(rows):
        y[i] = b[i] / UT[i][i]
        for k in range(i + 1, rows):
            b[k] -= UT[k][i] * y[i]
    print('Y:\n', y, '\n')
    x = np.zeros(rows)  
    for i in range(rows - 1, -1, -1):
        x[i] = y[i] / U[i][i]
        for k in range(i):
            y[k] -= U[k][i] * x[i]
    return x
    

def det(A):
    U = build_U(A)
    d = 1
    for i in range(U.shape[0]):
        d *= U[i][i] ** 2
    return d


def inversed_matrix_SQR(A):
    rows, cols = A.shape
    A_inv = np.zeros((rows, cols))
    for i in range(rows):
        b = np.zeros(rows)
        b[i] = 1
        U = build_U(A)
        cur_col = solve_sqrt(U, b)
        A_inv[:, i] = cur_col
    return  A_inv
        

def main():
    A = np.array([[3.389, 0.273, 0.126, 0.418],
                     [0.329, 2.796, 0.179, 0.278],
                     [0.186, 0.275, 2.987, 0.316],
                     [0.197, 0.219, 0.274, 3.127]])

    b = np.array([0.144, 0.297, 0.529, 0.869])
    A_symm, b_symm = symmetrize(A, b)
    print('A sim:\n', A_symm, '\n', 'B sim:\n', b_symm, '\n')
    # x = lab1.solve_gaussian(A_symm, b_symm)
    U = build_U(A_symm)
    print('U:\n', U, "\nU.T:\n", U.T, '\n')
    x1 = solve_sqrt(U, b_symm)
    a_det = det(A_symm)
    a_inv = inversed_matrix_SQR(A_symm)
    print('Result: ', x1)
    print('Determinant: ', a_det)
    print('Inversed matrix:\n', a_inv)
    

if __name__ == '__main__':
    main()

__all__ = ['symmetrize', 'inversed_matrix_SQR', 'det', 'solve_sqrt', 'build_U']
