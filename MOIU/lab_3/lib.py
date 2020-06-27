import numpy as np
from lab_1_2.lib import simplex


def start_phase(A, b):
    m, n = A.shape
    Jb = [n + i for i in range(m)]

    for i in range(m):
        if b[i] < 0:
            b[i] *= -1
            for j in range(n):
                A[i][j] *= -1

    x = [0] * n + b
    c = [0] * n + [-1] * m

    # print(*A)
    # print(x)

    A2 = np.hstack((A, np.eye(m)))
    print("A2: ", A2)
    print("Jb: ", Jb)
    print("c:", c)
    print("x:", x)

    print('=====')
    opt_pl, Jb_ans, max_pr = simplex(A2, c, x, Jb)
    print('=====')

    for j in range(m):
        if x[n + j] != 0:
            print("Задача несовместна!")
            return

    print(Jb_ans, " - базисный план симплекс метода")
    while True:
        i = -1
        bad_j = -1
        Jb_len = len(Jb_ans)
        for j in range(Jb_len):
            if Jb_ans[j] > n - 1:
                i = Jb_ans[j] - n + 1
                bad_j = j
                break

        if i == -1:
            print("A: ", A2)
            print("Задача совместна")
            print(x[: m], " - оптимальный план")
            print([i + 1 for i in Jb_ans], " - базисный план")
            return

        Ab = np.zeros((Jb_len, Jb_len))
        for k in range(Jb_len):
            Ab[:, k] = A2[:, Jb_ans[k]]

        is_end = False
        for j in range(n):
            if j not in Jb_ans:
                if np.linalg.det(Ab) == 0:
                    break
                l_j = np.dot(np.linalg.inv(Ab), A2[:, j])
                print("l_j: ", l_j)
                if l_j[bad_j] != 0:
                    Jb_ans[bad_j] = j
                    is_end = True
                    break

        if is_end:
            continue
        del Jb_ans[bad_j]
        A2 = np.delete(A2, bad_j, axis=0)
