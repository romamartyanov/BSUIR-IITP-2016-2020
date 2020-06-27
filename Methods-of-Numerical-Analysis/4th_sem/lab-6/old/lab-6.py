import numpy as np
from sympy import *
from matplotlib import pyplot as plt


def lagrange(x, y, x0):
    answer = 0

    for i in range(len(x)):
        x1 = 1
        x2 = 1

        for j in range(len(x)):
            if j != i:
                x1 *= x0 - x[j]
                x2 *= x[i] - x[j]

        answer += (x1 / x2) * y[i]
    return answer


def print_lagrange(x, y):
    x0 = symbols('x0')
    print("L = %.2f -  (%.2f - %.2f / %.2f - %.2f) * (x - %.2f) " % (y[0], y[1], y[0], x[1], x[0], x[0]))
    print(y[0] - (y[1] - y[0] / x[1] - x[0]) * (x - x[0]))


def finite_diff(x, y):
    print('\n')

    # temp_x = np.array([0.231, 0.848, 1.322, 2.224, 2.892])
    # temp_y = np.array([-2.748, -3.225, -3.898, -5.908, -6.506])

    temp_x = np.copy(x)
    temp_y = np.copy(y)

    for k in range(1, 5, 1):
        for i in range(len(temp_x) - k):
            temp_y[i] = temp_y[i + 1] - temp_y[i]
            #print('delta^{0}'.format(k), 'y{0} = '.format(i), temp_y[i])


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
            #print('delta^{0}'.format(k), 'y{0} = '.format(i), A[k][i])

    return A


def newton_polynom(x, y, x0):
    a = divided_diff(x, y)
    answer = 0

    for i in range(len(x)):
        b = 1

        for j in range(i):
            b *= x0 - x[j]

        answer += a[0][i] * b
    return answer


def linear_approx(x, y):
    a0 = np.zeros(len(x))
    a1 = np.zeros(len(x))

    for i in range(1, len(x)):
        a1[i-1] = (y[i] - y[i-1]) / (x[i] - x[i-1])
        a0[i-1] = y[i-1] - a1[i - 1] * x[i-1]

    print('a1 =', a1)
    print('a0 =', a0)
    return a1, a0


def quadratic_approx(x, y):
    a = np.zeros((len(x) - 2, 3))
    for i in range(1, len(x) - 1):
        a[i - 1, 2] = (y[i + 1] - y[i - 1]) / ((x[i + 1] - x[i - 1]) * (x[i + 1] - x[i])) - \
                      (y[i] - y[i - 1]) / ((x[i] - x[i - 1]) * (x[i + 1] - x[i]))

        a[i - 1, 1] = (y[i] - y[i - 1]) / (x[i] - x[i - 1]) - a[i - 1, 2] * (x[i] + x[i - 1])

        a[i - 1, 0] = y[i - 1] - a[i - 1, 1] * x[i - 1] - a[i - 1, 2] * x[i - 1] ** 2
    print(a)
    return a


def get_line_y(x, k, b):
    return k * x + b


def get_parabola_y(x, a, b, c):
    return a * x ** 2 + b * x + c


def cube_splines(x, y):
    n = len(x)
    h = np.zeros(n)
    l = np.zeros(n)

    delta = np.zeros(n)
    lam = np.zeros(n)

    a = np.zeros(n)
    b = np.zeros(n)
    c = np.zeros(n)
    d = np.zeros(n)

    a[:-1] = y[1:]
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

    for i in range(n - 1, 0, -1):
        c[i - 1] = delta[i - 1] * c[i] + lam[i - 1]

    for i in range(1, n - 1):
        b[i] = l[i] + 2 / 3 * c[i] * h[i] + 1 / 3 * h[i] * c[i - 1]
        d[i] = (c[i] - c[i - 1]) / (3 * h[i])

    b[0] = l[0] + 2 / 3 * c[0] * h[0]
    d[0] = c[0] / (3 * h[0])
    print('a =', a, '\nb =', b, '\nc =', c, '\nd =', d)
    return a, b, c, d


def get_cube_y(x0, a, b, c, d, xk):
    return a + b * (x0 - xk) + c * (x0 - xk) ** 2 + d * (x0 - xk) ** 3


def main():
    x = np.array([0.231, 0.848, 1.322, 2.224, 2.892])
    y = np.array([-2.748, -3.225, -3.898, -5.908, -6.506])

    xnew = np.linspace(x[0], x[-1], 100)
    # ynew = [makeLin(a, b, x, i) for i in xnew]
    xnew2 = np.linspace(x[0], x[-1], 100)
    ynew2 = [lagrange(x, y, i) for i in xnew2]
    # plt.plot(x, y, 'o', xnew, ynew, '-', xnew2, ynew2, '-')

    plt.plot(x, y, 'ro', label='points')
    xpts = np.arange(np.min(x), np.max(x), 0.01)

    ypts_lagrange = np.array([lagrange(x, y, t) for t in xpts])
    plt.plot(xpts, ypts_lagrange, label='Lagrange')

    ypts_newton = np.array([newton_polynom(x, y, t) for t in xpts])
    plt.plot(xpts, ypts_newton, label='Newton')

    a, b = linear_approx(x, y)
    ypts_linear = []
    xpts_linear = []
    for i in range(1, len(x)):
        cur_xpts = np.arange(x[i - 1], x[i], 0.01)
        xpts_linear += list(cur_xpts)
        ypts_linear += [get_line_y(t, a[i - 1], b[i - 1]) for t in cur_xpts]
    plt.plot(xpts_linear, ypts_linear, label='Linear spline')
    
    a = quadratic_approx(x, y)
    ypts_quadratic = []
    xpts_quadratic = []
    for i in range(1, len(x) - 1, 2):
        cur_xpts = np.arange(x[i - 1], x[i + 1], 0.01)
        xpts_quadratic += list(cur_xpts)
        ypts_quadratic += [get_parabola_y(t, a[i - 1, 2], a[i - 1, 1], a[i - 1, 0]) for t in cur_xpts]
    if i < len(x) - 3:
        cur_xpts = np.arange(x[-2], x[-1], 0.01)
        xpts_quadratic += list(cur_xpts)
        ypts_quadratic += [get_parabola_y(t, a[-1, 2], a[-1, 1], a[-1, 0]) for t in cur_xpts]
    plt.plot(xpts_quadratic, ypts_quadratic, label='Quadratic spline')

    a, b, c, d = cube_splines(x, y)
    xpts_cubic = []
    ypts_cubic = []
    for i in range(len(x) - 1):
        cur_xpts = np.arange(x[i], x[i + 1], 0.01)
        xpts_cubic += list(cur_xpts)
        ypts_cubic += [get_cube_y(t, a[i], b[i], c[i], d[i], x[i + 1]) for t in cur_xpts]

    plt.plot(xpts_cubic, ypts_cubic, label='Cubic spline')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=2, borderaxespad=0.)
    plt.show()

    print("L4(x1+x2) = " + str(lagrange(x, y, x[1] + x[2])))
    print("N4(x1+x2) = " + str(newton_polynom(x, y, x[1] + x[2])))
    finite_diff(x, y)
    divided_diff(x, y)
    linear_approx(x, y)
    quadratic_approx(x, y)


if __name__ == '__main__':
    main()
