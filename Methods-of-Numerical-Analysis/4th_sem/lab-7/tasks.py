import matplotlib.pyplot as plt
from source import *


def task_1(a, b, n):
    h, n = find_h(a, b, n)

    print("1:")
    print("Шаг = ", h)
    print()

    return h


def task_2(a, b, n, h):
    print("2:")
    print("По формуле трапеций")
    res, n, trapeze_h = trapeze(a, b, n)
    print("I =", res, "n =", n, "Шаг:", trapeze_h)

    res, n, trapeze_half_h = trapeze(a, b, n // 2)
    print("I =", res, "n =", n, "Шаг:", trapeze_half_h)

    maxfx2 = 4.386
    eps = maxfx2 * ((b - a) * h * h) / 12
    print("Уточненная погрешность h (трапеция):", eps)
    eps = maxfx2 * ((b - a) * 2 * h * 2 * h) / 12
    print("Уточненная погрешность 2h (трапеция):", eps)
    print()


def task_3(a, b, n, h):
    print("3:")
    print("По формуле Симпсона")
    res, n, simpson_h = simpson(a, b, n)
    print("I =", res, "n =", n, "Шаг:", simpson_h)

    res, n, simpson_half_h = simpson(a, b, n // 2)
    print("I =", res, "n =", n, "Шаг:", simpson_half_h)

    maxfx4 = -0.5
    eps = maxfx4 * ((b - a) * (h ** 4)) / 180
    print("Уточненная погрешность h (по Симпосона):", eps)

    eps = maxfx4 * ((b - a) * ((2 * h) ** 4)) / 180
    print("Уточненная погрешность 2h (по Симпосона):", eps)
    print()


def task_5(a, b, eps):
    h = eps ** (1 / 4)
    h = find_h_cauchy(a, b, h)
    print("Шаг =", h)
    print("n =", int((b - a) / h))

    return h


def task_6(a, b, h, y0):
    x_runge_h, y_runge_h = runge(a, b, h, y0)

    print("Рунге-Кутта h:")
    print("x:")
    print(*x_runge_h[::2], sep="\n")
    print()

    print("y:")
    print(*y_runge_h[::2], sep="\n")
    print()

    x_runge_2h, y_runge_2h = runge(a, b, 2 * h, y0)

    print("Рунге-Кутта 2h:")
    print("x:")
    print(*x_runge_2h, sep="\n")
    print()

    print("y:")
    print(*y_runge_2h, sep="\n")
    print()

    print("Дельта Рунге-Кутта")
    for i in range(len(y_runge_2h)):
        print(abs(y_runge_h[i * 2] - y_runge_2h[i]), end="\n")
    print()

    return x_runge_h, y_runge_h


def task_7(a, b, h, y0):
    x_adam_h, y_adam_h = adams(a, b, h, y0)

    print("Адамс h:")
    print("x:")
    print(*x_adam_h[::2], sep="\n")
    print()

    print("y:")
    print(*y_adam_h[::2], sep="\n")
    print()

    x_adam_2h, y_adam_2h = adams(a, b, 2 * h, y0)

    print("Адамс 2h:")
    print("x:")
    print(*x_adam_2h, sep='\n')
    print()

    print("y:")
    print(*y_adam_2h, sep='\n')
    print()

    print("Дельта Адамс")
    for i in range(len(y_adam_2h)):
        print(abs(y_adam_h[i * 2] - y_adam_2h[i]), end="\n")
    print()

    return x_adam_h, y_adam_h


def task_8(a, b, h, y0):
    x_euler_h, y_euler_h = euler(a, b, h, y0)

    print("Эйлер h:")
    print("x:")
    print(*x_euler_h[::2], sep='\n')
    print("y:")
    print(*y_euler_h[::2], sep='\n')
    print()

    x_euler_2h, y_euler_2h = euler(a, b, 2 * h, y0)

    print("Эйлер 2h:")
    print("x:")
    print(*x_euler_2h, sep='\n')
    print()

    print("y:")
    print(*y_euler_2h, sep='\n')
    print()

    print("Дельта Эйлера")
    for i in range(len(y_euler_2h)):
        print(abs(y_euler_h[i * 2] - y_euler_2h[i]), end="\n")
    print()

    return x_euler_h, y_euler_h


def plots(x_runge_h, y_runge_h, x_adam_h, y_adam_h, x_euler_h, y_euler_h):
    plt.plot(x_runge_h, y_runge_h, '-', x_adam_h, y_adam_h, '-', x_euler_h, y_euler_h, '-')
    plt.grid(True)
    plt.show()
