import numpy as np
import sympy as sp
from sympy import cos, sin, exp
import math
from matplotlib import pyplot as plt


def solve_diag(A, B, C, F):
    a = [0]
    b = [0]
    n = len(A)

    for i in range(n):
        a.append(-C[i] / (A[i] * a[i] + B[i]))
        b.append((F[i] - A[i] * b[i]) / (A[i] * a[i] + B[i]))

    y = np.zeros(n)
    y[n - 1] = (F[n - 1] - A[n - 1] * b[n - 1]) / (C[n - 1] + A[n - 1] * a[n - 1])
    for i in range(n - 2, -1, -1):
        y[i] = a[i + 2] * y[i + 1] + b[i + 2]

    return y


def f(a):
    def wrapped(x):
        return -1 / a

    return wrapped


# Builds coefficients for diff equation in format y'' - p(x)y = f(x)
def build_coeffs_tridiag(x_start, x_end, h, p, g):
    x = sp.symbols('x')

    A, B, C, F = [], [], [], []
    for xi in np.arange(x_start, x_end + h, h):
        A.append(1)
        C.append(1)
        B.append(-h ** 2 * p.subs({x: xi}) - 2)
        F.append(h ** 2 * g(xi))

    return A, B, C, F


def build_coeffs_tridiag_task4(x_start, x_end, h, p, g):
    x = sp.symbols('x')

    A, B, C, F = [], [], [], []
    for xi in np.arange(x_start, x_end + h, h):
        A.append(1)
        C.append(1)
        B.append(-h ** 2 * p(xi) - 2)
        F.append(h ** 2 * g(xi))

    A[0] = 3.6 + h
    B[0] = -4.8
    C[0] = 1.2
    F[0] = F[-1] = 0
    C[-1] = h + 1.2
    B[-1] = -1.5
    A[-1] = 0.4

    return A, B, C, F


def build_coeffs(x_start, x_end, h, p, q, g):
    x = sp.symbols('x')
    n = int((x_end - x_start) / h) + 1

    a = np.zeros((n, n))
    b = np.zeros(n)
    for i, xi in enumerate(np.arange(x_start + h, x_end, h)):
        j = i + 1
        a[j][j - 1] = 2
        a[j][j] = 2 * h ** 2 * q.subs({x: xi}) - h * p.subs({x: xi}) - 4
        a[j][j + 1] = 2 + h * p.subs({x: xi})
        b[j] = 2 * h ** 2 * g.subs({x: xi})

    a[0][0] = 2 * h ** 2 * q.subs({x: x_start}) - 3 * h * p.subs({x: x_start}) - 4
    a[0][1] = 2 + 4 * h * p.subs({x: x_start})
    a[0][2] = -h * p.subs({x: x_start})
    b[0] = 2 * h ** 2 * g.subs({x: x_start})

    a[n - 1][n - 1] = 2 * h ** 2 * q.subs({x: x_end}) - 3 * h * p.subs({x: x_end}) + 2
    a[n - 1][n - 2] = -4 - 4 * h * p.subs({x: x_end})
    a[n - 1][n - 3] = h * p.subs({x: x_end})
    b[n - 1] = 2 * h ** 2 * g.subs({x: x_end})

    return np.linalg.solve(a, b)


def solve_task1(e=0.001):
    var = int(input("Enter variant: "))
    a = math.sin(var)
    b = math.cos(var)
    p, x = sp.symbols("p x")
    p = -(1 + b * x ** 2) / a

    x_start = -1
    x_end = 1

    h = 0.25
    cur_precision = 1

    print('Solving task1: ')
    print("y'' + (" + str(p) + ') * y = ' + str(-1 / a))
    print('q = ' + str(p))
    print('p = 0')
    print('x0 = ' + str(x_start))
    print('xn = ' + str(x_end))
    print('Start step = ' + str(h))

    A, B, C, F = build_coeffs_tridiag(x_start, x_end, h * 2, p, f(a))
    y1 = solve_diag(A, B, C, F)
    y = []

    while cur_precision > e:
        y = np.copy(y1)
        h /= 2
        A, B, C, F = build_coeffs_tridiag(x_start, x_end, h, p, f(a))
        y1 = solve_diag(A, B, C, F)
        cur_precision = np.max(np.abs([y1[2 * i] - y[i] for i in range(len(y))]))
        print('Precision: {}, Current step: {}'.format(cur_precision, h))

    x1 = np.arange(x_start, x_end + h, h)
    plt.plot(x1, y1)
    plt.show()


def solve_task2(e=0.05):
    p, q, g, x = sp.symbols("p q g x")
    p = cos(x) ** 2
    q = 10 / (1 + sin(x) ** 2)
    g = exp(-0.5 * x) * (12 - x ** 2)

    x_start = 0
    x_end = 2
    h = 0.1

    cur_precision = 1
    y1 = build_coeffs(x_start, x_end, h, p, q, g)
    y = []

    while cur_precision > e:
        y = np.copy(y1)
        h /= 2
        y1 = build_coeffs(x_start, x_end, h, p, q, g)
        cur_precision = np.max(np.abs([y1[2 * i] - y[i] for i in range(len(y))]))
        print('Precision: {}, Current step: {}'.format(cur_precision, h))

    plt.plot(np.arange(x_start, x_end + h, h), y1)
    plt.show()


def build_coeffs1(x_start, x_end, h, p, q, g):
    x = sp.symbols('x')
    n = int((x_end - x_start) / h) + 1

    a = np.zeros((n, n))
    b = np.zeros(n)
    for i, xi in enumerate(np.arange(x_start + h, x_end, h)):
        j = i + 1
        a[j][j - 1] = 2
        a[j][j] = 2 * h ** 2 * q.subs({x: xi}) - h * p.subs({x: xi}) - 4
        a[j][j + 1] = 2 + h * p.subs({x: xi})
        b[j] = 2 * h ** 2 * g.subs({x: xi})

    a[0][0] = -3
    a[0][1] = 4
    a[0][2] = -1
    b[0] = 0

    a[n - 1][n - 1] = 2 * h - 3
    a[n - 1][n - 2] = 12
    a[n - 1][n - 3] = -3
    b[n - 1] = 4 * h

    return np.linalg.solve(a, b)


def solve_task3(e=0.07):
    p, q, g, x = sp.symbols("p q g x")
    p = -4 * x
    q = 5 + 0 * x
    g = 2 * x

    x_start = 2
    x_end = 4
    h = 0.1

    print('Solving task 2: ')
    print("y'' + (" + str(p) + ") * y' + (" + str(q) + ') * y = ' + str(g))
    print('q = ' + str(p))
    print('p = ' + str(q))
    print('x0 = ' + str(x_start))
    print('xn = ' + str(x_end))
    print('Start step = ' + str(h))

    cur_precision = 1
    y1 = build_coeffs1(x_start, x_end, h, p, q, g)
    y = []

    while cur_precision > e:
        y = np.copy(y1)
        h /= 2
        y1 = build_coeffs1(x_start, x_end, h, p, q, g)
        cur_precision = np.max(np.abs([y1[2 * i] - y[i] for i in range(len(y))]))
        print('Precision: {}, Current step: {}'.format(cur_precision, h))

    plt.plot(np.arange(x_start, x_end + h, h), y1)
    plt.show()


def solve_task4():
    p, x = sp.symbols("p x")
    k1 = 1.2
    k2 = 0.4
    q1 = 8.3
    q2 = 2.8
    g = 9 / (2 + 0.3 * x ** 2)
    c = 1.875
    k = lambda xi: k1 if xi < c else k2
    q = lambda xi: q1 if xi < c else q2

    x_start = 0
    x_end = 2.8

    h = 0.25
    cur_precision = 1
    e = 0.05

    print('Solving task 3: ')
    print("y'' + q(x) / k(x) * y = " + str(g) + "/ k(x)")
    print('q = q(x) / k(x)')
    print('p = 0')
    print('x0 = ' + str(x_start))
    print('xn = ' + str(x_end))
    print('Start step = ' + str(h))

    A, B, C, F = build_coeffs_tridiag_task4(x_start,
                                            x_end,
                                            h * 2,
                                            lambda xi: -q(xi) / k(xi),
                                            lambda xi: -g.subs({x: xi}) / k(xi)
                                            )

    y1 = solve_diag(A, B, C, F)
    y = []

    while cur_precision > e:
        y = np.copy(y1)
        h /= 2
        A, B, C, F = build_coeffs_tridiag_task4(x_start,
                                                x_end,
                                                h,
                                                lambda xi: -q(xi / k(xi)),
                                                lambda xi: -g.subs({x: xi}) / k(xi)
                                                )
        y1 = solve_diag(A, B, C, F)
        cur_precision = np.max(np.abs([y1[2 * i] - y[i] for i in range(len(y) - 1)]))
        print('Precision: {}, Current step: {}'.format(cur_precision, h))

    x1 = np.arange(x_start, x_end + h, h)
    plt.plot(x1, y1)
    plt.show()


def main():
    e = 0.001
    # solve_task1(e)
    solve_task2()
    # solve_task3()
    # solve_task4()


if __name__ == "__main__":
    main()
