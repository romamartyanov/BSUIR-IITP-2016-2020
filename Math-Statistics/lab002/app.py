import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as sts
import math


def get_bins_count(n):
    if n <= 100:
        return int(np.sqrt(n))
    else:
        return int(np.log(n))


def f(x):
    return 1 / (x + 3)


def g(y):
    return -1 / 10 * (1 / y - 13)


def h(y):
    return 0.1 / (y ** 2)


n = 100

a = 0
b = 10

ksi = []
if not n or n == 1:
    ksi = [0.2]
else:
    for i in range(n):
        ksi.append(np.random.uniform(0, 1))

X = [t * (b - a) + a for t in ksi]
Y = [f(x) for x in X]

Y = sorted(Y)
counts = {}

for y in Y:
    counts[y] = counts.get(y, 0) + 1

F = [0]

for i in range(len(Y) - 1):
    F.append(F[i] + counts[Y[i]] / n)

plt.plot(Y, F)

G = [g(y) for y in Y]
plt.plot(Y, F, Y, G)
dots_y = []
dots_x = []
for j in range(len(F) - 1):
    for i in range(100):
        dots_x.append(Y[j] + i * (Y[j + 1] - Y[j]) / 100)
        dots_y.append(F[j])

for i in range(10):
    dots_x.append(Y[-1] + i / 100)
    dots_y.append(1)

plt.plot(dots_x, dots_y, Y, G)
plt.xlabel('y')
plt.ylabel('Функция распределения')
plt.grid(True)

plt.show()

###

y_min = Y[0]

y_max = Y[-1]
delta = (y_max - y_min) / n

borders_equalinterval = [(y_min + delta * i) for i in range(1, len(Y) + 1)]
plt.hist(Y, get_bins_count(n), normed=1)

H = [h(y) for y in Y]
plt.plot(Y, H)
plt.show()

###

borders_equiprobable = get_bins_count(n)

borders_eq = [Y[0]] + [(Y[i] + Y[i + 1]) / 2
                       for i in range(borders_equiprobable - 1, n - 1, n // borders_equiprobable)] + [Y[-1]]

plt.hist(Y, bins=borders_eq, normed=1)
plt.plot(Y, H)
plt.show()


###


def xi_2(sample, a):
    n = len(sample)
    m = get_bins_count(n)
    v = n // m
    borders = [sample[0]] + [(sample[i * v - 1] + sample[i * v]) / 2.0 for i in range(1, m)] + [sample[m * v - 1]]
    p = [float(v) / n] * m

    p_t = [g(borders[i]) - g(borders[i - 1]) for i in range(1, len(borders))]

    # p_t -> частость попадания в i'й интервал
    # p -> теоретическая вероятность попадания СВ в интервал
    # a -> альфа (уровень значимости)
    # k = M-1-S = len(p)-1 -> число степеней свободы

    chi_chi = n * sum([(p[i] - p_t[i]) ** 2 / p_t[i] for i in range(len(p))])
    # print(p)
    # print(p_t)

    if chi_chi <= sts.chi2.ppf(1 - a, len(p) - 1):
        print('Не отклоняем выдвинутую гипотезу (Критерий хи-квадрат Пирсона):\n '
              'хи квадртат: {chi}, табличный хи-квадрат: {table_chi}'.format(chi=chi_chi,
                                                                             table_chi=sts.chi2.ppf(1 - a, len(
                                                                                 p) - 1)))
    else:
        print('Отклоняем выдвинутую гипотезу (Критерий хи-квадрат Пирсона):\n '
              'хи квадртат: {chi}, \nтабличный хи-квадрат: {table_chi}'.format(chi=chi_chi,
                                                                               table_chi=sts.chi2.ppf(1 - a, len(
                                                                                   p) - 1)))


def kolmg(sample):
    n = len(sample)

    # модуль максимальной разности между теоретической и эмпирической функции распределения
    # значение критерия sqrt(n) * d

    d = max([abs(i / n - g(sample[i])) for i in range(n)] + [abs((i - 1) / n - g(sample[i])) for i in range(n)])
    lam = math.sqrt(n) * d

    print(lam)

    if 1.63 > lam:
        print("Не отклоняем выдвинутую гипотезу (критерий Колмогорова)")

    else:
        print("Отклоняем выдвинутую гипотезу (критерий Колмогорова)")


def mizes(sample):
    n = len(sample)

    # критерий -> средний квадрат отклонений по всем аргументам х
    # a = 0.01 -> фактической значение

    d = [(g(sample[i]) - (i - 0.5) / n) ** 2 for i in range(n)]
    t = (1.0 / (12 * n) + sum(d))
    print(t)
    if 0.744 > (1.0 / (12 * n) + sum(d)):
        print("Не отклоняем выдвинутую гипотезу (Критерий Мизеса)")

    else:
        print("Отклоняем выдвинутую гипотезу (Критерий Мизеса)")
    return d


def sample(n):
    a = 0
    b = 10

    ksi = []
    if not n or n == 1:
        ksi = [0.2]
    else:
        for i in range(n):
            ksi.append(np.random.uniform(0, 1))

    X = [t * (b - a) + a for t in ksi]
    Y = [f(x) for x in X]

    Y = sorted(Y)

    return Y


def show_sample(Y, n):
    borders_equiprobable = get_bins_count(n)

    borders_eq = [Y[0]] + [(Y[i] + Y[i + 1]) / 2
                           for i in range(borders_equiprobable - 1, n - 1, n // borders_equiprobable)] + [Y[-1]]

    plt.hist(Y, bins=borders_eq, normed=1)
    H = [h(y) for y in Y]
    plt.plot(Y, H)
    plt.show()


xi_2_sample = sample(200)
xi_2(xi_2_sample, 0.05)
show_sample(xi_2_sample, 200)
print()

kolmg_sample = sample(30)
kolmg(kolmg_sample)
show_sample(kolmg_sample, 30)
print()

mizes_sample = sample(50)
mizes(mizes_sample)
show_sample(mizes_sample, 50)
print()
