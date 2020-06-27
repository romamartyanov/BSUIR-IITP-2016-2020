from sympy import *
import math as math


def f(x):
    return 4*(x**2 + 1) * math.log(x) - 1


def df(x):
    return 8 * x * math.log(x) + (1/x * (4 * x**2 + 4))


def method_chord():
    e = 0.001
    a = 1.0
    b = 2.0

    x_k = [a, b]

    if f(a) * f(b) < 0:
        n = 0
        x_0 = x_k[0]

        while (x_0 - x_k[1] > e) or (x_k[1] - x_0 > e):
            n += 1
            x_0 = x_k[1]

            print('x_k[0]: ', x_k[0])
            print('x_0: ', x_0)

            x_k[1] = x_k[0] - (f(x_k[0]) / (f(x_k[1]) - f(x_k[0])) * (x_k[1] - x_k[0]))

            print('x_k[1]', x_k[1], '\n')

            x_k[0] = x_0

    print('Root in [{}, {}]: '.format(a, b), 'i:  ', x_k[1], ', in ', n, 'iterations')


def method_tangents():
    e = 0.001
    a = 1.0
    x_0 = a
    x_1 = x_0 - (f(x_0) / df(x_0))
    n = 0
    while (x_0 - x_1 > e) or (x_1 - x_0 > e):
        n += 1
        print('x_0 = ', x_0)
        print('x_1 = ', x_1)
        x_0 = x_1
        x_1 = x_0 - (f(x_0) / df(x_0))
    print('Root in [{}, {}]:'.format(a, 2.0), x_1, ', in ', n, 'iterations')


def msi():
    x, y = symbols('x y')
    e = 0.01
    _x = (1 - sin(x + y)) / 1.2
    _y = sqrt(1 - x**2)
    print('x = ', _x)
    print('y = ', _y)
    x_0, y_0 = 1.0, 0.5

    x_1, y_1 = _x.subs(x, x_0).subs(y, y_0), _y.subs(x, x_0).subs(y, y_0)
    n = 1
    while abs(x_0 - x_1) > e or abs(y_0 - y_1) > e:
        x_0, y_0 = x_1, y_1
        x_1, y_1 = _x.subs(x, x_0).subs(y, y_0), _y.subs(x, x_0).subs(y, y_0)
        n += 1
    print('by MSI:\n x: ', x_1, ', y: ', y_1, ', n: ', n)
    print(nsolve([sin(x + y) + 1.2 * x - 1, x**2 + y**2 - 1], [x, y], [1, 0.5]))


def nm():
    x, y = symbols('x y')

    e = 0.001
    f_1 = sin(x + y) + 1.2 * x - 1
    f_2 = x**2 + y**2 - 1

    func = Matrix([f_1, f_2])
    j = Matrix([[diff(f_1, x), diff(f_1, y)], [diff(f_2, x), diff(f_2, y)]])
    v_0 = Matrix([1.0, 0.5])

    v_1 = (v_0 - j.inv() * func).subs(x, v_0[0]).subs(y, v_0[1])
    n = 1
    while abs(v_0[0] - v_1[0]) > e and abs(v_0[1] - v_1[1]) > e:
        v_0 = v_1
        v_1 = (v_0 - j.inv() * func).subs(x, v_0[0]).subs(y, v_0[1])
        n += 1

    print('\nby MN:\n x: ', v_1[0], ', y: ', v_1[1], ', n: ', n)


def modif_nm():
    x, y = symbols('x y')

    e = 0.01
    f_1 = sin(x + y) + 1.2 * x - 1
    f_2 = x**2 + y**2 - 1

    func = Matrix([f_1, f_2])
    v_0 = Matrix([1.0, 0.5])

    j = Matrix([[diff(f_1, x), diff(f_1, y)], [diff(f_2, x), diff(f_2, y)]])
    j_inv = j.inv().subs(x, v_0[0]).subs(y, v_0[1])

    v_1 = (v_0 - j_inv * func).subs(x, v_0[0]).subs(y, v_0[1])

    n = 1
    while abs(v_0[0] - v_1[0]) > e or abs(v_0[1] - v_1[1]) > e:
        v_0 = v_1
        v_1 = (v_0 - j_inv * func).subs(x, v_0[0]).subs(y, v_0[1])
        n += 1

    print('\nby modified MN:\n x: ', v_1[0], ', y: ', v_1[1], ', n: ', n)


def main():
    x, y = symbols('x y')

    fi = plot(ln(x), (x, 1, 3), show=False)
    psi = plot(1 / (4 * (1 + x**0.5)), line_color='r', show=False)
    fi.extend(psi)
    fi.show()
    
    sys_1 = plot_implicit(Eq(sin(x + y) - 1.2 * x, 1), show=False)
    sys_2 = plot_implicit(Eq(x**2 + y**2, 1), show=False, line_color='r')
    sys_1.extend(sys_2)
    sys_1.show()

    method_chord()
    print()
    method_tangents()
    print()

    print('SNE:')
    pprint(Eq(sin(x + y) + 1.2 * x, 1))
    pprint(Eq(x**2 + y**2 - 1, 1))
    print()

    msi()
    print()
    nm()
    print()
    # modif_nm()
    print()


if __name__ == '__main__':
    main()


