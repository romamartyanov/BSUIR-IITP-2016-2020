from tasks import *


def main():
    a = 1
    b = 2
    n = 4

    h = task_1(a, b, n)
    task_2(a, b, n, h)
    task_3(a, b, n, h)

    ###

    a = 0
    b = 1
    eps = 0.0001
    y0 = 1

    h = task_5(a, b, eps)
    x_runge_h, y_runge_h = task_6(a, b, h, y0)
    x_adam_h, y_adam_h = task_7(a, b, h, y0)
    x_euler_h, y_euler_h = task_8(a, b, h, y0)

    plots(x_runge_h, y_runge_h, x_adam_h, y_adam_h, x_euler_h, y_euler_h)


if __name__ == "__main__":
    main()
