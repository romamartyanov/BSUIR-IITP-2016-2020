import numpy as np
import matplotlib.pyplot as plt


def lagrange(x,x_set,y_set):
    lnx = 0

    px = 1
    for i in range(len(x_set)):
        for j in range(len(x_set)):
            if i != j:
                px *= (x - x_set[j]) / (x_set[i] - x_set[j])
        lnx += px * y_set[i]
        px = 1
    return lnx


def main():
    x_set = [0.172, 0.567, 1.113, 2.119, 2.769]
    y_set = [-7.057, -5.703, -0.132, 1.423, 2.832]
    x = 0.567 + 1.113
    print("L4(x):", lagrange(x, x_set, y_set))

    xnew = np.linspace(x_set[0], x_set[-1], 100)
    ynew = [lagrange(i, x_set, y_set) for i in xnew]
    plt.plot(x_set, y_set, 'o', xnew, ynew)
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()