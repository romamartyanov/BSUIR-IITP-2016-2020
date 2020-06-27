import numpy as np
from scipy.optimize import linprog


def g_x(x, B, c, alpha):
    return 0.5 * x.T.dot(B.T).dot(B).dot(x) + c.T.dot(x) + alpha


def df_dx(x, B, c):
    return B.T.dot(B).dot(x) + c


def generate_all_g(x, B, c, alpha):
    return np.array([g_x(x, B[i], c[i], alpha[i]) for i in range(len(alpha))])


def convex_method(B0, c0, B, c, alpha, x, debug=False):
    J0 = [i for i in range(len(x)) if x[i] == 0]

    g = generate_all_g(x, B, c, alpha)
    print("{0} - начальный план".format(x) if (g <= 0).all() else exit())

    if debug:
        print("Значение целевой функции по начальному плану f(x) = {0}".format(g_x(x, B0, c0, 0.0)))
        print("Проверка оптимальности начального плана...")
    I0 = np.array([i for i in range(len(g)) if 0 <= abs(g[i]) <= 1.0e-4])
    if debug:
        print("g: ", g)
        print("I0: ", I0)
    df = df_dx(x, B0, c0)
    linear_condition = np.array([df_dx(x, B[i], c[i]) for i in range(len(c))])
    if debug:
        print("df/dx: ", *df)
        print("Linear condition:", *linear_condition, sep='\n')
    upper_bounds = np.ones(len(x))
    lower_bounds = [0 if i in J0 else -1 for i in range(len(x))]
    solve = linprog(df,
                    A_ub=linear_condition,
                    b_ub=np.zeros(len(linear_condition)),
                    bounds=list(zip(lower_bounds, upper_bounds)),
                    method='simplex')
    print(solve)
    print('План не оптимален, dg/dx = ', solve.fun if solve.fun < 0 else exit())

    delta_x  = np.zeros(len(x)) - x
    b = delta_x.dot(df)
    a0 = - solve.fun / b
    if b > 0:
        a = a0 / 2
    else:
        a = 1

    t = 1
    while True:
        x_t = x + t * solve.x + a * t * delta_x
        if (generate_all_g(x, B, c, alpha) <= 0).all() and (x_t >= 0).all():
            break
        t /= 2

    print("Новый план x_t = ", *list(map(lambda v: round(v, 4), x_t)))
    print("Новое значение целевой функции f(x,t) = ", g_x(x_t, B0, c0, 0))


def main():
    B0 = np.array([[2, 1, 0, 4, 0, 3, 0, 0],
                   [0, 4, 0, 3, 1, 1, 3, 2],
                   [1, 3, 0, 5, 0, 4, 0, 4]])
    B1 = np.array([[0, 0, 0.5, 2.5, 1, 0, -2.5, -2],
                  [0.5, 0.5, -0.5, 0, 0.5, -0.5, -0.5, -0.5],
                  [0.5, 0.5, 0.5, 0, 0.5, 1, 2.5, 4]])
    B2 = np.array([[1, 2, -1.5, 3, -2.5, 0, -1, -0.5],
                   [-1.5, -0.5, -1, 2.5, 3.5, 3, -1.5, -0.5],
                   [1.5, 2.5, 1, 1, 2.5, 1.5, 3, 0]])
    B3 = np.array([[0.75, 0.5, -1, 0.25, 0.25, 0, 0.25, 0.75],
                   [-1, 1, 1, 0.75, 0.75, 0.5, 1, -0.75],
                   [0.5, -0.25, 0.5, 0.75, 0.5, 1.25, -0.75, -0.25]])
    B4 = np.array([[1.5, -1.5, -1.5, 2, 1.5, 0, 0.5, -1.5],
                   [-0.5, -2.5, -0.5, -1, -2.5, 2.5, 1, 2],
                   [-2.5, 1, -2, -1.5, -2.5, 0.5, 2.5, -2.5]])
    B5 = np.array([[1, 0.25, -0.5, 1.25, 1.25, -0.5, 0.25, -0.75],
                   [-1, -0.75, -0.75, 0.5, -0.25, 1.25, 0.25, -0.5],
                   [0, 0.75, 0.5, -0.5, -1, 1, -1, 1]])
    B = [B1, B2, B3, B4, B5]

    c0 = np.array([-1, -1, -1, -1, -2, 0, -2, -3])
    c = np.array([[0, 60, 80, 0, 0, 0, 40, 0],
                  [2, 0, 3, 0, 2, 0, 3, 0],
                  [0, 0, 80, 0, 0, 0, 0, 0],
                  [0, -2, 1, 2, 0, 0, -2, 1],
                  [-4, -2, 6, 0, 4, -2, 60, 2]])
    alpha = np.array([-51.75, -436.75, -33.7813, -303.3750, -41.75])
    x = np.array([1, 0, 0, 2, 4, 2, 0, 0])

    print(0.5 * x.dot(B[0].T).dot(B[0]).dot(x))
    print(c[0].dot(x) + alpha[0])

    convex_method(B0, c0, B, c, alpha, x, True)


if __name__ == '__main__':
    main()
