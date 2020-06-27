import matplotlib.pyplot as plt

from Interpolation import *


def task_1(x_set, y_set, x):
    print(x_set)
    print("L4(x1+x2): ", lagrange(x_set, y_set, x))
    print()

    x_new = np.linspace(x_set[0], x_set[-1], 100)
    y_new = [lagrange(x_set, y_set, i) for i in x_new]
    plt.plot(x_set, y_set, 'o', x_new, y_new)
    plt.grid(True)
    plt.show()


def task_2(x_set, y_set):
    print("Конечные разности: ")
    finite_diff(y_set, len(y_set))
    print()

    print("Разделенные разности: ")
    # divided_diff(x_set, y_set, len(y_set), 0)

    print()


def task_3(x_set, y_set):
    print("Полином Ньютона: ")
    newts = []
    newts = kdiff(x_set, y_set, len(y_set), 0, newts)
    # newton(1.68, x_set, y_set, newts)
    # newton(x_set, y_set, newts)
    print("N4(x1+x2) = " + str(newton(x_set, y_set, x_set[1] + x_set[2])))
    print()


def task_4(x, y):
    a, b = linear(x, y)
    print("Кусочно-линейные коэффициенты:")
    print(a)
    print(b)
    print()

    a1, b1, c1 = quadratic(x, y)
    print("Кусочно-квадратичные коэффициенты:")
    print(a1)
    print(b1)
    print(c1)
    print()

    x_new = np.linspace(x[0], x[-1], 100)
    y_new = [lagrange(x, y, i) for i in x_new]

    x_new2 = np.linspace(x[0], x[-1], 100)
    y_new2 = [make_lin(a, b, x, i) for i in x_new]

    x_new3 = np.linspace(x[0], x[-1], 100)
    y_new3 = [make_quadratic(a1, b1, c1, x, i) for i in x_new3]

    # plt.plot(x, y, 'o', x_new3, y_new3, '-', x_new2, y_new2, '-', x_new, y_new, '-')
    plt.plot(x, y, 'o', x_new, y_new, '-', x_new2, y_new2, '-')
    plt.grid(True)
    plt.show()

    plt.plot(x, y, 'o', x_new, y_new, '-', x_new3, y_new3, '-')
    plt.grid(True)
    plt.show()


def task_5(x, y):
    a, b, c, d = cube(x, y)

    print('Интерполяционный кубический сплайн (коэфиценты):')
    print('a', a)
    print('b', b)
    print('c', c)
    print('d', d)

    x_new = np.linspace(x[0], x[-1], 100)
    y_new = [lagrange(x, y, i) for i in x_new]

    x_new1 = np.linspace(x[0], x[-1] - 0.01, 1000)
    y_new1 = [make_cube(a, b, c, d, x, i) for i in x_new1]

    plt.plot(x, y, 'o', x_new, y_new, '-', x_new1, y_new1, '-')

    plt.grid(True)
    plt.show()


def task_6(x, y):
    a1, b1 = linear(x, y)
    a2, b2, c2 = quadratic(x, y)
    a3, b3, c3, d3 = cube(x, y)

    x_new = np.linspace(x[0], x[-1], 100)
    y_new = [lagrange(x, y, i) for i in x_new]

    x_new1 = np.linspace(x[0], x[-1], 100)
    y_new1 = [make_lin(a1, b1, x, i) for i in x_new1]

    x_new2 = np.linspace(x[0], x[-1], 100)
    y_new2 = [make_quadratic(a2, b2, c2, x, i) for i in x_new2]

    x_new3 = np.linspace(x[0], x[-1] - 0.01, 1000)
    y_new3 = [make_cube(a3, b3, c3, d3, x, i) for i in x_new3]

    plt.plot(x, y, 'o', x_new, y_new, '-', x_new1, y_new1, '-', x_new2, y_new2, '-', x_new3, y_new3, '-')

    # plt.plot(x, y, 'o', x_new, y_new, '-', x_new2, y_new2, '-')
    #
    # plt.plot(x, y, 'o', x_new, y_new, '-', x_new1, y_new1, '-')

    # a2, b2, c2, d2 = cubic_approx(x, y)
    # xpts_cubic = []
    # ypts_cubic = []
    # for i in range(len(x) - 1):
    #     cur_xpts = np.arange(x[i], x[i + 1], 0.01)
    #     xpts_cubic += list(cur_xpts)
    #     ypts_cubic += [get_cube_y(t, a2[i], b2[i], c2[i], d2[i], x[i + 1]) for t in cur_xpts]
    #
    # plt.plot(xpts_cubic, ypts_cubic, label='Cubic spline')
    # plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
    #            ncol=2, borderaxespad=0.)

    plt.grid(True)
    plt.show()
