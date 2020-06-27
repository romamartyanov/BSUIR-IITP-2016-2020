from collections import OrderedDict
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import scipy.stats as sts

import random
import math


def get_m(n):
    if n <= 100:
        m = int(math.sqrt(n))
    else:
        m = int(3 * math.log(n, 10))
    return m


def f(x):
    return 1 / (x + 3)


def distribution_f(y):
    return -1 / 10 * (1 / y - 13)


def density(y):
    return 0.1 / (y ** 2)


def sample(a, b, n):
    x_range = list()
    y_range = list()

    for i in range(n):
        e = random.random()
        x = (b - a) * e + a

        x_range.append(x)
        y_range.append(f(x))

    return x_range, y_range


def pirs_criterion(y_range):
    """
    Показывает расхождение между теоретическим и эмпирическим распределением,
    которая приближенно подчиняется закону распределения хи^2

    """
    y_range.sort()

    n = len(y_range)
    M = get_m(n)

    v = int(n / M)

    histogram = OrderedDict()
    i = v - 1

    # рассчитываю отрезки для равновероятн гист
    histogram[(y_range[0], y_range[v - 1])] = v

    while i + v < n:
        histogram[(y_range[i], y_range[i + v])] = v
        i += v

    if i < n - 1:
        histogram[(y_range[i], y_range[-1])] = n - i  # -1

    xi_square_sum = 0
    control_sum = 0

    for key in histogram.keys():
        # для каждого отрезка гист
        v_i = histogram[key]

        # высоту ее столбика
        f_i = v_i / n / (key[1] - key[0])

        p_i_f = distribution_f(key[1]) - distribution_f(key[0])

        # рассчитал, прибавил к общей сумме.
        #  ниже - для контрольного соотношения тоже к сумме прибавил
        xi_square_sum += (((v_i - p_i_f * n) ** 2) / (p_i_f * n))
        control_sum += p_i_f

        histogram[key] = (v_i, f_i, p_i_f, xi_square_sum)
        # записал все в свой словарь для гист

    # print("\nРавновероятностный метод")
    table = PrettyTable(field_names=["Ai", "Bi", "v", "f", "Pi", "xi_i"])
    for (key, v) in histogram.items():
        table.add_row((key[0], key[1], v[0], v[1], v[2], v[3]))

    # print(table, '\n')

    print("Xi^2: ", xi_square_sum)

    # print("Проверим контрольное соотношение: | 1 -", control_sum, "| < 0.01 is", abs(1 - control_sum) <= 0.01)

    key = M - 1 - 0
    print("Количество степеней свободы  К: ", key)

    f_bars = plt.figure("Равновероятностная гистограмма")
    bars = []

    for (key, v) in histogram.items():
        width = abs(key[1] - key[0])

        bars.append(plt.bar(x=key[0],
                            width=width,
                            height=v[1],
                            align="edge"))

    (x_coords, y_coords) = build_plot(y_range, density)
    plt.plot(x_coords, y_coords, color='red')
    f_bars.show()

    print("Хи квадрат: ", xi_square_sum,
          "\nХи из таблицы: ", sts.chi2.ppf(1 - 0.05, M - 1))


def empyrical_distribution_function(y_range):
    """

    """
    n = len(y_range)

    y_range.sort()

    y_function = []
    y_c = [0]
    for i, val in enumerate(y_range[1:], start=1):
        previous = y_range[i - 1]

        if val == previous:
            continue
        else:
            y_function.append((previous, val, i / n))

        y_c.append(i / n)

    x_coords = []
    y_coords = []

    pre_h = 0
    fig = plt.figure("DF")

    for i, piece in enumerate(y_function[:-1]):
        x_coords += [piece[0], piece[1], piece[1]]
        y_coords += [pre_h, y_function[i][2], y_function[i + 1][2]]

        pre_h = y_function[i + 1][2]

    plt.plot(x_coords, y_coords, color='red')

    return y_c


def kolmogorov_criteria(x_range):
    """
    В качестве меры расхождения теор. и эмпирич. ФР непрерывной СВ используется
    модуль максимальной разности
    """
    y_empiric = empyrical_distribution_function(x_range)

    (x_c, y_c) = build_plot(x_range, distribution_f)
    plt.plot(x_c, y_c, color="green")
    plt.show()

    n = len(y_empiric)
    # print(len(y_empiric) == len(y_c))

    maximum = 0

    table = PrettyTable(field_names=["x", "F*(x)", "F0(x)", "d"])
    for i in range(n):
        d = abs(y_c[i] - y_empiric[i])

        table.add_row(row=(x_range[i], y_empiric[i], y_c[i], d))
        maximum = max(maximum, d)

    # print(table, '\n')
    # print("**************************************")

    alpha = 0.01
    gamma = 1 - alpha

    print("\nmax|F*(x) - F0(x)| = ", maximum)
    lambda_p = math.sqrt(n) * maximum

    print("Значение критерия (lambda): ", lambda_p)
    print("Уровень значимости alpha:", alpha, "\nДоверительная вероятность gamma =", gamma)
    print("Табличный лямбда: 1.63")


def mises_criteria(x_range):
    """
    В качестве меры различия
    выступает средний квадрат отклонения по всем значениям аргумента х

    """
    y_empiric = empyrical_distribution_function(x_range)

    (x_c, y_c) = build_plot(x_range, distribution_f)
    stat_sum = 0

    n = len(x_range)
    table = PrettyTable(field_names=["x", "F*(x)", "F0(x)", "d**2"])

    for i in range(n):
        d = abs(y_c[i] - y_empiric[i]) ** 2
        stat_sum += (y_c[i] - (i - 0.5) / n) ** 2

        table.add_row(row=(x_range[i], y_empiric[i], y_c[i], d))

    # print(table, '\n')

    nw2 = 1 / (12 * n) + stat_sum

    print("\nnw^2: ", nw2)
    print("табличный критерий: 0.744")


def build_plot(y_range, f):
    x_coords = []
    y_coords = []

    for i in y_range:
        x_coords.append(i)
        y_coords.append(f(i))

    return x_coords, y_coords


def main():
    a = 0
    b = 10

    x_range, y_range = sample(a, b, 200)
    # print("Вариационный ряд Х (для Пиррса):", x_range)
    # print("Вариационный ряд У (для Пиррса): ", y_range, '\n\n')
    print("Критерий Пирсона")
    pirs_criterion(y_range)
    print('\n\n')

    x_range, y_range = sample(a, b, 30)
    # print("Вариационный ряд Х (для Колмогорова):", x_range)
    # print("Вариационный ряд У (для Колмогорова): ", y_range, '\n\n')
    print("Критерий Колмогорова")
    kolmogorov_criteria(y_range)
    print('\n\n')

    x_range, y_range = sample(a, b, 50)
    # print("Вариационный ряд Х (для Колмогорова):", x_range)
    # print("Вариационный ряд У (для Колмогорова): ", y_range, '\n\n')
    print("Критерий Мизеса")
    mises_criteria(y_range)
    print('\n\n')


if __name__ == '__main__':
    main()
