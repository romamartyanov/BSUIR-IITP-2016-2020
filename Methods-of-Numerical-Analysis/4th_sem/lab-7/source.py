import math


def f_numerical_int(x):
    return x ** 2 * math.log(x)


def f_cauchy(x, y):
    return 2 * (x ** 3 * y ** 3) - 2 * x * y


##########################################################


def find_h(a, b, n):
    prev = 0
    res, n_trapeze, h = trapeze(a, b, n)

    while abs(res - prev) > 0.001:
        prev = res
        n += 4
        res, n_trapeze, h = trapeze(a, b, n)

    return (b - a) / n, n


def trapeze(a, b, n):
    h = (b - a) / n
    x = a
    res = 0
    for i in range(n + 1):
        if i == 0 or i == n:
            res += f_numerical_int(x) / 2
        else:
            res += f_numerical_int(x)
        x += h
    res *= h

    # print("I =", res, "n =", n,  "Шаг:", h)
    return res, n, h


def simpson(a, b, n):
    h = (b - a) / n
    x = a
    res = 0

    for i in range(n + 1):
        if i == 0 or i == n:
            res += f_numerical_int(x) / 2

        elif i % 2 == 1:
            res += 2 * f_numerical_int(x)

        else:
            res += f_numerical_int(x)
        x += h

    res *= (2 * h) / 3
    return res, n, h


##################################################


def runge(a, b, h, y0, k=None):
    y_arr = list()
    x_arr = list()
    y_arr.append(y0)

    n = int((b - a) / h)
    for i in range(n + 1):
        x_arr.append(a + h * i)

    for i in range(0, n):
        f1 = f_cauchy(x_arr[i], y_arr[i])
        f2 = f_cauchy(x_arr[i] + h / 2, y_arr[i] + (h / 2) * f1)
        f3 = f_cauchy(x_arr[i] + h / 2, y_arr[i] + (h / 2) * f2)
        f4 = f_cauchy(x_arr[i + 1], y_arr[i] + h * f3)

        y_new = y_arr[i] + (h / 6) * (f1 + 2 * f2 + 2 * f3 + f4)

        y_arr.append(y_new)

    if k is None:
        return x_arr, y_arr
    else:
        return y_arr[k - 1]


# def runge_special(a, b, h, y0, wave):
#     y_set = list()
#     x_set = list()
#     y_set.append(y0)
#
#     if wave:
#         k = 2
#     else:
#         k = 3
#
#     for i in range(k):
#         x_set.append(a + h * i)
#
#     for i in range(k - 1):
#         k1 = f(x_set[i], y_set[i])
#         k2 = f(x_set[i] + h / 2, y_set[i] + (h / 2) * k1)
#         k3 = f(x_set[i] + h / 2, y_set[i] + (h / 2) * k2)
#         k4 = f(x_set[i + 1], y_set[i] + h * k3)
#         y_new = y_set[i] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
#         y_set.append(y_new)
#
#     print(x_set)
#     print(y_set)
#
#     return y_set[-1]


def adams(a, b, h, y0):
    n = int((b - a) / h)
    y_arr = list()
    x_arr = list()

    for i in range(n + 1):
        x_arr.append(a + h * i)

    y_arr.append(y0)
    temp = round(y_arr[0] + h * f_cauchy(x_arr[0], y_arr[0]), 6)  # Считаем по методу Эйлера
    y_arr.append(temp)

    for i in range(1, n):
        temp = round(y_arr[i] + (h / 2) * (3 * f_cauchy(x_arr[i], y_arr[i]) - f_cauchy(x_arr[i - 1], y_arr[i - 1])), 6)
        y_arr.append(temp)

    return x_arr, y_arr


def euler(a, b, h, y0):
    n = int((b - a) / h)
    y_set = list()
    x_set = list()

    for i in range(n + 1):
        x_set.append(a + h * i)

    y_set.append(y0)
    for i in range(0, n):
        temp = round(y_set[i] + h * f_cauchy(x_set[i], y_set[i]), 6)
        y_set.append(temp)

    return x_set, y_set


def find_h_cauchy(a, b, h):
    y2_h = 0
    y2_2h = 0.5

    while (1 / 15) * abs(y2_h - y2_2h) >= 0.0001:
        y2_h = runge(a, b, h, 2, 3)
        y2_2h = runge(a, b, 2 * h, 2, 2)
        h /= 2

    return h
