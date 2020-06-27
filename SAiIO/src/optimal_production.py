import numpy as np


def restore_path(B, X, c):
    path = []
    for i in range(len(B) - 1, -1, -1):
        path.append(X[i, c])
        c -= X[i, c]

    path.reverse()
    return path


def solve(F, c):
    n, m = np.shape(F)
    B = np.zeros((n, m), dtype=np.int32)
    X = np.zeros((n, m), dtype=np.int32)

    B[0] = F[0]
    X[0] = list(range(m))

    for i in range(1, n):
        for j in range(m):
            b_max = 0
            b_max_pos = 0

            for k in range(j + 1):
                b = F[i][k] + B[i - 1][j - k]

                if b > b_max:
                    b_max = b
                    b_max_pos = k

            B[i][j] = b_max
            X[i][j] = b_max_pos

    path = restore_path(B, X, c)

    return path, B
