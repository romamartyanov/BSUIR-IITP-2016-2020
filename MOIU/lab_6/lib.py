import numpy as np


def quadratic_programming_problem(A, d, x, J_op, J, B, debug=False):
    D = np.dot(B.T, B)
    c = - np.dot(d.T, B)
    J -= 1
    J_op -= 1
    m, n = A.shape
    iteration = 0
    skip_1 = False
    j0 = 0

    while True:
        iteration += 1

        print('==================================================================================')
        if not skip_1:
            not_J_op = np.delete(np.arange(n), J_op)
            c_x = c + np.dot(x, D)
            A_op_inv = np.linalg.inv(A[:, J_op])
            u_x = - c_x[J_op].dot(A_op_inv)
            delta = u_x.dot(A) + c_x
            round_delta = np.array(list(map(lambda _x: round(float(_x), 4), delta)))

            if (round_delta >= 0).all():
                print()
                print(list(map(lambda _x: round(float(_x), 3), list(x))), " - оптимальный план")
                print("max = ", round(c.dot(x) + 0.5 * x.dot(D).dot(x), 4))
                print("Количество итераций: ", iteration)
                return x.tolist(), c.dot(x) + 0.5 * x.dot(D).dot(x), iteration

            else:
                ind = np.argmin(delta[not_J_op])
                j0 = not_J_op[ind]

        skip_1 = False
        l = np.zeros(n)
        l[j0] = 1

        len_J = len(J)
        H = np.zeros((m + len_J, m + len_J))
        H[:len_J, :len_J], H[len_J:, :len_J], H[:len_J, len_J:] = D[J][:, J], A[:, J], A[:, J].T

        b_z = np.zeros(m + len_J)
        b_z[: len_J], b_z[len_J:] = D[j0][J], A[:, j0]

        x_kr = np.linalg.inv(H).dot(-b_z)
        l[J] = x_kr[: len_J]

        theta = [-x[i] / l[i] if l[i] < 0 else np.inf for i in J]
        j_z = np.argmin(theta)

        small_delta = l.T.dot(D).dot(l)
        theta_j0 = np.inf if 0 < abs(small_delta) <= 1.0e-10 else np.abs(delta[j0] / small_delta)
        theta_0, j_z = (theta_j0, j0) if theta[j_z] >= theta_j0 else (theta[j_z], J[j_z])

        if debug:
            print('*****************************')
            print("Итерация: %d" % iteration)
            print("H:")
            print(*H, sep='\n')
            print("l = ", *l)
            print("j0 = ", j0)
            print("j* = ", j_z)
            print("theta_0 = ", theta_0)
            print("delta = ", *delta)
            print('*****************************')

            print()

        if np.isinf(theta_0):
            print("Нет решения, так как целевая функция не ограничена на множестве допустимых планов")
            return
        x = x + theta_0 * l
        if debug:
            print("Новый план: ", x)

        if j0 == j_z:  # case 1
            J = np.append(J, j_z)

        elif j_z in set(J) - set(J_op):  # case 2
            J = J[J != j_z]
            delta[j0] += theta_0 * small_delta
            skip_1 = True
            J_op.sort()
            J.sort()

        else:
            s = np.where(J_op == j_z)
            e_s = np.eye(m)[s]
            j_plus = set(J) - set(J_op)

            print("J_plus", j_plus)

            t = list(filter(lambda i: e_s.dot(A_op_inv).dot(A[:, i]) != 0, j_plus))
            print("t: ", t)

            if t:  # case 3
                J_op = np.append(J_op[J_op != j_z], int(t[0]))
                J = J[J != j_z]
                delta[j0] += theta_0 * small_delta
                skip_1 = True
                J_op.sort()
                J.sort()

            else:  # case 4
                J_op = np.append(J_op[J_op != j_z], j0)
                J = np.append(J[J != j_z], j0)

        if debug:
            print("J_op = ", J_op)
            print("J* = ", J)
