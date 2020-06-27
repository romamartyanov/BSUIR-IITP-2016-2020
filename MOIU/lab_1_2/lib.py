import numpy as np


def inv_matrix(A, A_inv, x, i):
    A_kr = np.copy(A)
    A_kr[:, i] = x
    l = np.dot(A_inv, x)
    if l[i] == 0:
        return False
    l_v = np.copy(l)
    l_v[i] = -1
    l_kr = - l_v / l[i]
    Q = np.eye(len(x))
    Q[:, i] = l_kr
    return np.dot(Q, A_inv)


def simplex(A, c, x, Jb):
    iter_count = 0
    Jb = [i - 1 for i in Jb]
    last_inv = None

    while True:
        p = len(Jb)
        is_optimal = False
        Ab = np.zeros((p, p))
        c_b = []

        for i, j in enumerate(Jb):
            Ab[:, i] = A[:, j]
            c_b.append(c[j])

        if last_inv is not None:
            Ab_inv = inv_matrix(Ab, last_inv, A[:, j0], s)
        else:
            Ab_inv = np.linalg.inv(Ab)

        last_inv = Ab_inv

        u = np.dot(c_b, Ab_inv)

        delta = np.dot(u, A) - c

        J_notb = [i for i, j in enumerate(delta) if j < 0 and i not in Jb]

        if len(J_notb) == 0:
            is_optimal = True

        if is_optimal:
            opt_pl = list(map(lambda _x: round(float(_x), 3), list(x)))
            max_pr = round(float(np.dot(c, x)), 4)

            print(opt_pl, "- оптимальный план")
            print("Максимальная прибыль : ", max_pr)
            print("Количество итераций : ", iter_count)

            return opt_pl, Jb, max_pr

        j0 = J_notb[0]
        z = np.dot(Ab_inv, A[:, j0])

        theta = []
        for i in range(len(z)):
            if z[i] > 0:
                theta.append(x[Jb[i]] / z[i])
            else:
                theta.append(np.inf)

        min_theta = np.min(theta)

        if min_theta == np.inf:
            print("Целевая функция неограничена сверху!")
            return "Целевая функция неограничена сверху!"

        s = theta.index(min_theta)
        Jb[s] = j0
        x[j0] = min_theta

        # print("Jb", Jb)
        for i in range(len(x)):
            if i not in Jb:
                x[i] = 0

        for i, j in enumerate(Jb):
            if i != s:
                x[j] = x[j] - z[i] * min_theta

        iter_count += 1
