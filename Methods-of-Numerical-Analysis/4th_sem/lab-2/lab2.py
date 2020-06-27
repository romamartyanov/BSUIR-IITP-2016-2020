import numpy


def prepare_system(A, b):
    rows, cols = A.shape
    a = A.copy()
    b1 = b.copy()

    for i in range(rows):
        b1[i] /= a[i][i]
        a[i, :] = -a[i, :] / a[i][i]
        a[i][i] = 0

    return a, b1


def solve_iterations(a, b, e, start_x, max_iterations=10000):
    cur_x = start_x.copy()
    prev_x = start_x.copy()

    final_iteration = max_iterations

    for i in range(max_iterations):
        cur_x = numpy.dot(a, cur_x) + b

        print(cur_x, numpy.linalg.norm(cur_x - prev_x))
        print('=========')

        if numpy.linalg.norm(cur_x - prev_x) < e:
            final_iteration = i
            break

        prev_x = cur_x.copy()

    return cur_x, final_iteration + 1


def solve_zeidel(a, b, e, start_x, max_iterations=10000):
    cur_x = start_x.copy()
    prev_x = start_x.copy()

    final_iteration = max_iterations
    n = a.shape[0]

    def get_LU(a):
        L = numpy.zeros(a.shape)
        U = numpy.zeros(a.shape)

        rows = a.shape[0]

        for i in range(rows):
            L[i, :i] = a[i, :i]
            U[i, i:] = a[i, i:]
        return L, U

    L, U = get_LU(a)
    E = numpy.identity(n)

    for i in range(max_iterations):
        cur_x = numpy.dot(
                            numpy.dot(
                                        numpy.linalg.inv(E - L), U
                                    ), cur_x
                        ) + numpy.dot(numpy.linalg.inv(E - L), b)

        print(cur_x, numpy.linalg.norm(cur_x - prev_x))
        print('----------')

        if numpy.linalg.norm(cur_x - prev_x) < e:
            final_iteration = i
            break

        prev_x = cur_x.copy()

    return cur_x, final_iteration + 1


def convergence_condition(a):
    x = 1
    norm = numpy.linalg.norm(a)
    if norm < x:
        print('Не выполняется условие сходимости')
        quit()


def main():
    A = numpy.array([[3.389, 0.273, 0.126, 0.418],
                     [0.329, 2.796, 0.179, 0.278],
                     [0.186, 0.275, 2.987, 0.316],
                     [0.197, 0.219, 0.274, 3.127]])

    b = numpy.array([0.144, 0.297, 0.529, 0.869])
    e = 0.01

    a, beta = prepare_system(A, b)
    start_x = numpy.zeros(len(beta))

    # Проверка условий сходимости решения
    convergence_condition(a)

    x, iterations = solve_iterations(a, beta, e, start_x)
    print()
    x1, zeidel = solve_zeidel(a, beta, e, start_x)

    print()
    print(x, iterations)
    print()
    print(x1, zeidel)


if __name__ == '__main__':
    main()
