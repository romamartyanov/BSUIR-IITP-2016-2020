import numpy as np


def lagrange(x_set, y_set, x):
    answer = 0
    product = 1
    for i in range(len(x_set)):
        for j in range(len(y_set)):
            if i != j:
                product *= (x - x_set[j]) / (x_set[i] - x_set[j])
        answer += product * y_set[i]
        product = 1
    return answer


def finite_diff(y_set, set_len):
    new_set = []
    if set_len == 1:
        return y_set

    for i in range(set_len - 1):
        new_set.append(y_set[i + 1] - y_set[i])
    print(new_set)

    finite_diff(new_set, len(new_set))


# def divided_diff(x_set, y_set, set_len, k):
#     new_y_set = []
#
#     if set_len == 1:
#         return y_set
#
#     for i in range(set_len - 1):
#         n = (y_set[i + 1] - y_set[i]) / (x_set[i + k + 1] - x_set[i])
#         new_y_set.append(n)
#
#     print(new_y_set)
#     k += 1
#     divided_diff(x_set, new_y_set, len(new_y_set), k)


def kdiff(x_set, y_set, set_len, k, newton_set):
    new_y_set = []

    if set_len == 1:
        return newton_set

    for i in range(set_len - 1):
        n = (y_set[i + 1] - y_set[i]) / (x_set[i + k + 1] - x_set[i])
        new_y_set.append(n)

    print(new_y_set)
    newton_set.append(new_y_set[0])
    k += 1

    newton_set = kdiff(x_set, new_y_set, len(new_y_set), k, newton_set)
    return newton_set

#
# def newton(x, x_set, y_set, newton_s):
#     n_x = y_set[0]
#
#     for i in range(len(newton_s)):
#         temp = newton_s[i]
#
#         for j in range(i + 1):
#             temp *= x - x_set[j]
#         n_x += temp
#
#     print("N4(x):", n_x)


def divided_diff(x, y):
    # temp_x = np.array([0.231, 0.848, 1.322, 2.224, 2.892])
    # temp_y = np.array([-2.748, -3.225, -3.898, -5.908, -6.506])

    temp_x = np.copy(x)
    temp_y = np.copy(y)

    A = np.zeros((len(temp_x), len(temp_x) + 1))
    A[:, 0] = temp_y

    for i in range(1, 5, 1):
        for k in range(len(temp_x) - i):
            A[k, i] = (A[k + 1, i - 1] - A[k, i - 1]) / (temp_x[k + i] - temp_x[k])

    return A


def newton(x, y, x0):
    a = divided_diff(x, y)
    answer = 0

    for i in range(len(x)):
        b = 1

        for j in range(i):
            b *= x0 - x[j]

        answer += a[0][i] * b

    print(answer)
    return answer


def linear(x_set, y_set):
    a_set = []
    b_set = []
    for i in range(1, len(x_set)):
        a_set.append(round((y_set[i] - y_set[i - 1]) / (x_set[i] - x_set[i - 1]), 3))
        b_set.append(round((y_set[i - 1] - a_set[i - 1] * x_set[i - 1]), 3))

    return a_set, b_set


def quadratic(x_set, y_set):
    a_set = []
    b_set = []
    c_set = []

    for i in range(1, len(x_set) - 1):
        c_set.append(round(
            (y_set[i + 1] - y_set[i - 1]) / ((x_set[i + 1] - x_set[i - 1]) * (x_set[i + 1] - x_set[i])) - (
                        y_set[i] - y_set[i - 1]) / ((x_set[i] - x_set[i - 1]) * (x_set[i + 1] - x_set[i])), 3))

        b_set.append(
            round((y_set[i] - y_set[i - 1]) / (x_set[i] - x_set[i - 1]) - c_set[i - 1] * (x_set[i] + x_set[i - 1]), 3))

        a_set.append(round(y_set[i - 1] - b_set[i - 1] * x_set[i - 1] - c_set[i - 1] * x_set[i - 1] ** 2, 3))

    return a_set, b_set, c_set


def make_lin(a, b, x, t):
    ind = 0
    len_x_range = len(x)

    for i in range(len_x_range):
        if x[i] > t:
            ind = i
            break

    return a[ind - 1] * t + b[ind - 1]


def make_quadratic(a, b, c, x, t):
    ind = 0
    len_x_range = len(x) - 1

    for i in range(len_x_range):
        if x[i] > t:
            ind = i
            break

    return c[ind - 1] * t ** 2 + b[ind - 1] * t + a[ind - 1]


def make_cube(a, b, c, d, x, t):
    ind = 0
    len_x_range = len(x)

    for i in range(len_x_range):
        if x[i] > t:
            ind = i
            break

    return a[ind - 1] + b[ind - 1] * (t - x[ind]) + c[ind - 1] * (t - x[ind]) ** 2 + d[ind - 1] * (t - x[ind]) ** 3


def get_line_y(x, k, b):
    return k * x + b


def get_cube_y(x0, a, b, c, d, xk):
    return a + b * (x0 - xk) + c * (x0 - xk) ** 2 + d * (x0 - xk) ** 3


def cube(x, y):
    h = [0] * len(x)
    l = [0] * len(x)
    len_x_range = len(x) - 1

    for i in range(len_x_range):
        h[i] = round(x[i + 1] - x[i], 3)
        l[i] = round((y[i + 1] - y[i]) / h[i], 3)

    delta = [0] * len(x)
    lamb = [0] * len(x)

    delta[0] = -0.5 * h[1] / (h[0] + h[1])
    lamb[0] = 1.5 * (l[1] - l[0]) / (h[1] + h[0])

    len_x_range = len(x)
    for i in range(2, len_x_range):
        delta[i - 1] = - h[i] / (2 * h[i - 1] + 2 * h[i] + h[i - 1] * delta[i - 2])

    for i in range(2, len_x_range):
        lamb[i - 1] = (2 * l[i] - 3 * l[i - 1] - h[i - 1] * lamb[i - 2]) / (
                    2 * h[i - 1] + 2 * h[i] + h[i - 1] * delta[i - 2])

    c = [0] * len(x)
    b = [0] * len(x)
    d = [0] * len(x)
    a = [0] * len(x)

    len_x_range = len(x) - 1
    for i in range(len_x_range, 0, -1):
        c[i - 1] = round(delta[i - 1] * c[i] + lamb[i - 1], 3)

    a[:-1] = y[1:]

    for i in range(0, len_x_range):
        b[i] = round(l[i] + 2 / 3 * c[i] * h[i] + 1 / 3 * h[i] * c[i - 1], 3)
        d[i] = round((c[i] - c[i - 1]) / (3 * h[i]), 3)

    return a, b, c, d


def cubic_approx(x, y):
    n = len(x)
    h = np.zeros(n)
    l = np.zeros(n)

    delta = np.zeros(n)
    lam = np.zeros(n)

    for i in range(n - 1):
        h[i] = x[i + 1] - x[i]
        l[i] = (y[i + 1] - y[i]) / h[i]

    delta[0] = - 1 / 2 * h[1] / (h[0] + h[1])
    lam[0] = 3 / 2 * (l[1] - l[0]) / (h[1] + h[0])

    for i in range(2, n):
        delta[i - 1] = - h[i] / (2 * h[i - 1] + 2 * h[i] + h[i - 1] * delta[i - 2])

    for i in range(2, n):
        lam[i - 1] = (2 * l[i] - 3 * l[i - 1] - h[i - 1] * lam[i - 2]) / (
            2 * h[i - 1] + 2 * h[i] + h[i - 1] * delta[i - 2])

    c = np.zeros(n)
    a = np.zeros(n)

    a[:-1] = y[1:]
    b = np.zeros(n)
    d = np.zeros(n)

    for i in range(n - 1, 0, -1):
        c[i - 1] = delta[i - 1] * c[i] + lam[i - 1]

    for i in range(1, n - 1):
        b[i] = l[i] + 2 / 3 * c[i] * h[i] + 1 / 3 * h[i] * c[i - 1]
        d[i] = (c[i] - c[i - 1]) / (3 * h[i])

    b[0] = l[0] + 2 / 3 * c[0] * h[0]
    d[0] = c[0] / (3 * h[0])

    return a, b, c, d
