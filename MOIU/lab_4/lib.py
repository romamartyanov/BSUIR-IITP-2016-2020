from numpy import *


def double_simplex(c, b, a_matrix, j_vector):
    m, n = a_matrix.shape
    iter_count = 1
    j_vector -= 1
    y = get_initial_y(c, a_matrix, j_vector)
    x_0 = [0 for _ in range(n)]

    print('============================================')

    while True:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        not_J = delete(arange(n), j_vector)
        B = linalg.inv(a_matrix[:, j_vector])
        print('B: \n', B)
        kappa = B.dot(b)

        if all(kappa >= 0):
            for j, _kappa in zip(j_vector, kappa):
                x_0[j] = _kappa

            print('****************************************')

            print("Количество итераций : ", iter_count)
            print("Максимальная прибыль : ", c.dot(x_0))
            print(list(map(lambda _x: round(float(_x), 3), list(x_0))), "-  план")
            print('****************************************')

            print('============================================')

            return x_0, iter_count

        k = argmin(kappa)
        delta_y = B[k]
        mu = delta_y.dot(a_matrix)

        print("mu: \n\t", mu)
        print("y: \n\t", y)

        sigma = []
        for i in not_J:
            if mu[i] >= 0:
                sigma.append(inf)

            else:
                sigma.append((c[i] - a_matrix[:, i].dot(y)) / mu[i])

        print("sigma:\n\t", sigma)

        sigma_0_ind = not_J[argmin(sigma)]
        sigma_0 = min(sigma)

        print("Sigma: \n\tval: {0} \n\tindex: {1}".format(sigma_0, sigma_0_ind))

        if sigma_0 == inf:
            print("Задача не имеет решения, т.к. пусто множество ее допустимых планов.")
            return "Задача не имеет решения"

        y += sigma_0 * delta_y
        j_vector[k] = sigma_0_ind
        iter_count += 1


def get_initial_y(c, a_matrix, j_vector):
    return (c[j_vector]).dot(linalg.inv(a_matrix[:, j_vector]))
