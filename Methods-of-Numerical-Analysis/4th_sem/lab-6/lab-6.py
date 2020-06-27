from Tasks import *


def main():
    x_set = np.array([0.231, 0.848, 1.322, 2.224, 2.892])
    y_set = np.array([-2.748, -3.225, -3.898, -5.908, -6.506])

    x = 0.848 + 1.322

    task_1(x_set, y_set, x)
    task_2(x_set, y_set)
    task_3(x_set, y_set)
    task_4(x_set, y_set)
    task_5(x_set, y_set)
    task_6(x_set, y_set)


if __name__ == "__main__":
    main()
