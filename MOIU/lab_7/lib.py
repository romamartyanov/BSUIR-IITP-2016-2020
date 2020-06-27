import numpy as np
from scipy.optimize import linprog


def transform_arrays(*args):
    return tuple(map(np.array, args))


def f(B_f, c_f, x):
    return c_f.dot(x) + 0.5 * x.dot(B_f.T).dot(B_f).dot(x)


def check_sleiter(B, c, a, x):
    return all(get_g_values(B, c, a, x) < 0)


def check_plan_validity(B, c, a, x):
    return all(get_g_values(B, c, a, x) <= 0)


def get_quadratic_norm_differential(Q, c, x, i):
    return x.T.dot(Q[i]) + c[i]


def get_function_differentials(B_f, c_f, x):
    Q = B_f.T.dot(B_f)
    return np.array([get_quadratic_norm_differential(Q, c_f, x, i) for i in range(len(x))])


def get_g_values(B, c, a, x):
    return np.array([f(B[i], c[i], x) + a[i] for i in range(len(a))])


def get_zero_positions(vec):
    return [i for i, val in enumerate(vec) if abs(val) < 0.0001]


def get_final_solution(B_f, c_f, B, c, a_values, x_kr, x_til, f_diffs, l):
    t = 0.5

    while t > 0.0000001:
        print('-----------------------------------------')
        print('f_diffs:\n{}\nl:\n{}'.format(f_diffs, l))

        a = f_diffs.dot(l)
        b = (x_kr - x_til).dot(f_diffs)
        alpha = 1

        if b > 0:
            alpha = - a / (2 * b)
        x_sol = x_til + t * l + alpha * t * (x_kr - x_til)

        plan_valid = check_plan_validity(B, c, a_values, x_sol)

        start_func_val = f(B_f, c_f, x_til)
        res_func_val = f(B_f, c_f, x_sol)

        print()
        print('a: {}, b: {}, alpha: {}, t: {}'.format(a, b, alpha, t))
        print('f(x~) =', start_func_val)
        print('f(x^) =', res_func_val)
        print('Plan valid?', plan_valid)

        print('-----------------------------------------')

        if plan_valid and res_func_val < start_func_val:
            return x_sol

        t /= 2

    raise OverflowError('Minimum t exceeded, solution not found')


def solve(B_f, c_f, B, c, a, x_til, x_kr):
    B_f, c_f, B, c, a, x_kr, x_til = transform_arrays(
        B_f, c_f, B, c, a, x_kr, x_til)

    slieter_result = check_sleiter(B, c, a, x_kr)
    if not slieter_result:
        print('Sleiter check failure')

    f_diffs = get_function_differentials(B_f, c_f, x_til)
    print('f (differentials):', f_diffs)

    g_values = get_g_values(B, c, a, x_til)
    print('g (values):', g_values)

    get_function_differentials(B[0], c[0], x_til)
    g_zero_positions = get_zero_positions(g_values)
    linear_system_conditions = np.array([get_function_differentials(B[i], c[i], x_til) for i in g_zero_positions])

    print()
    print('Linear conditions:')
    print(linear_system_conditions)

    upper_bounds = [1 for _ in x_til]
    lower_bounds = [-1 if abs(x_val) > 0.0001 else 0 for x_val in x_til]

    print('upper bounds:', upper_bounds)
    print('lower bounds:', lower_bounds)

    linear_system_solution = linprog(
        f_diffs,
        A_ub=linear_system_conditions,
        b_ub=np.zeros(len(linear_system_conditions)),
        bounds=list(zip(lower_bounds, upper_bounds)),
        method='simplex')

    print('--------------------')
    print('Linear system solution:')
    print(linear_system_solution)
    if not linear_system_solution['success']:
        print('No linear system solution')
        raise Exception('No linear system solution')

    l = linear_system_solution['x']
    f_l = f_diffs.dot(l)

    print('--------------------')

    print()
    print('Result df/dx*(l):\n', f_l)

    print('========== fin ===========')
    solution = get_final_solution(B_f, c_f, B, c, a, x_kr, x_til, f_diffs, l)
    print('==========================')

    print()
    print()
    print('SOLUTION:\n', solution)

    return solution
