import math
import matplotlib.pyplot as plt
import numpy as np

def main():
    x = [0.172, 0.567, 1.113, 2.119, 2.769]
    y = [-7.057, -5.703, -0.132, 1.423, 2.832]
    a, b = linear(x, y)
    print("Линейные коэффициенты:")
    print(a)
    print(b)
    a1, b1, c1 = quadratic(x, y)
    print("Квадратичные коэффициенты:")
    print(a1)
    print(b1)
    print(c1)

    xnew = np.linspace(x[0], x[-1], 100)
    ynew = [makeLin(a, b, x, i) for i in xnew]
    xnew2 = np.linspace(x[0], x[-1], 100)
    ynew2 = [lagran(x, y, i) for i in xnew2]
    xnew3 = np.linspace(x[0], x[-1], 100)
    ynew3 = [makeQuadr(a1, b1, c1, x, i) for i in xnew3]
    plt.plot(x, y, 'o', xnew3, ynew3, '-', xnew2, ynew2, '-', xnew, ynew, '-')
    # plt.plot(x, y, 'o', xnew2, ynew2, '-', xnew3, ynew3, '-')
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

    return a[ind-1]*t + b[ind-1]


def makeQuadr(a, b, c, x, t):
    ind = 0
    for i in range(len(x)-1):
        if x[i] > t:
            ind = i
            break

    return c[ind-1] * t ** 2 + b[ind-1] * t + a[ind-1]


if __name__ == "__main__":
    main()

