import math
import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.array([0.231, 0.848, 1.322, 2.224, 2.892])
    y = np.array([-2.748, -3.225, -3.898, -5.908, -6.506])

    a, b = linear(x, y)
    a1, b1, c1 = quadratic(x, y)
    a2, b2, c2, d2 = cubic_approx(x, y)
    xnew = np.linspace(x[0], x[-1], 100)
    ynew = [makeLin(a, b, x, i) for i in xnew]
    xnew2 = np.linspace(x[0], x[-1], 100)
    ynew2 = [lagran(x, y, i) for i in xnew2]
    xnew3 = np.linspace(x[0], x[-1], 100)
    ynew3 = [makeQuadr(a1, b1, c1, x, i) for i in xnew3]
    xnew4 = np.linspace(x[0], x[-1], 100)
    ynew4 = [makeCub(a2, b2, c2, d2, x, i) for i in xnew4]
    plt.plot(x, y, 'o', xnew3, ynew3, '-', xnew2, ynew2, '-', xnew, ynew, '-', xnew4, ynew4, '-')
    # plt.plot(x, y, 'o', xnew, ynew, '-', xnew2, ynew2, '-')
    plt.grid(True)
    plt.show()


def linear(x_set, y_set):
    a_set = []
    b_set = []
    for i in range(1,len(x_set)):
        a_set.append(round((y_set[i] - y_set[i-1]) / (x_set[i]-x_set[i-1]), 3))
        b_set.append(round((y_set[i-1] - a_set[i-1] * x_set[i-1]), 3))
    return a_set, b_set


def lagran(xArr, yArr, x):
    rez = 0
    proiz = 1
    for i in range(len(xArr)):
        for j in range(len(yArr)):
            if i != j:
                proiz *= (x - xArr[j]) / (xArr[i] - xArr[j])
        rez += proiz * yArr[i]
        proiz = 1
    return rez


def quadratic(x_set, y_set):
    a_set = []
    b_set = []
    c_set = []
    for i in range(1,len(x_set)-1):
        c_set.append(round((y_set[i+1]-y_set[i-1])/((x_set[i+1]-x_set[i-1])*(x_set[i+1]-x_set[i])) - (y_set[i]-y_set[i-1])/(( x_set[i]-x_set[i-1])*(x_set[i+1]-x_set[i])),3))
        b_set.append(round((y_set[i]-y_set[i-1])/(x_set[i]-x_set[i-1]) - c_set[i-1]*(x_set[i] + x_set[i-1]),3))
        a_set.append(round(y_set[i-1]-b_set[i-1]*x_set[i-1] - c_set[i-1] * x_set[i-1] ** 2, 3))
    return a_set, b_set, c_set


def makeLin(a, b, x, t):
    ind = 0
    for i in range(len(x)):
        if x[i] > t:
            ind = i
            break
        #ind = i

    return a[ind-1]*t + b[ind-1]


def makeQuadr(a, b, c, x, t):
    ind = 0
    for i in range(len(x)-1):
        if x[i] > t:
            ind = i
            break
        #ind = i

    return c[ind-1] * t ** 2 + b[ind-1] * t + a[ind-1]


def makeCub(a, b, c, d, x, t):
    ind = 0
    for i in range(len(x)):
        if x[i] > t:
            ind = i
            break
        #ind = i

    return a[ind-1] + b[ind-1] * (t - x[ind-1]) + c[ind-1] * (t-x[ind-1]) ** 2 + d[ind-1] * (t-x[ind-1]) ** 3


def cubic_approx(x, y):
    n = len(x) - 1
    h = [x[i + 1] - x[i] for i in range(n)]
    al = [3 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1]) for i in range(1, n)]
    al.insert(0, 0)

    l = [1] * (n + 1)
    u = [0] * (n + 1)
    z = [0] * (n + 1)
    for i in range(1, n):
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * u[i - 1]
        u[i] = h[i] / l[i]
        z[i] = (al[i] - h[i - 1] * z[i - 1]) / l[i]

    b = [0] * (n + 1)
    c = [0] * (n + 1)
    d = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        c[i] = z[i] - u[i] * c[i + 1]
        b[i] = (y[i + 1] - y[i]) / h[i] - h[i] * (c[i + 1] + 2 * c[i]) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])
    return [y, b, c, d]


if __name__ == "__main__":
    main()

