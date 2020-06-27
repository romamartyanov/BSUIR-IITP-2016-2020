import numpy as np
from sympy import *


def approximation(h):
    x = []
    y = []
    for i, v in enumerate(np.arange(-1, 1+h, h)):
        x.append(v)
        y.append(Symbol('y{}'.format(i)))

    s = []

    for i in range(1, len(x)-1):
        s.append((y[i+1] - 2 * y[i] + y[i-1]) / (h**2) + (1 + (x[i]**2)) * y[i] + 1)
    s.append(y[0])
    s.append(y[-1])
    print("System:", s)
    sol = next(iter(linsolve(s, y)))
    #print(sol)
    return x, sol


def main():
    precision = 1
    h = 0.5
    x, y = approximation(1)

    iter_num = 1
    while precision > 0.02:
        x_new, y_new = approximation(h)
        print(y_new)
        print(y)
        precision = sum([abs(y_new[2 * i] - y[i]) for i in range(len(y))])
        x, y = x_new, y_new
        h /= 2
        iter_num += 1
        print('iteration', iter_num)
        print('precision', precision)
        print('h', h)

    # pylab.scatter(x, y, color='black')
    # pylab.show()


if __name__ == "__main__":
    main()
