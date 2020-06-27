import numpy as np
import matplotlib.pyplot as plt


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


def get_line_y(x, k, b):
    return k * x + b


def makeCub(a, b, c, d, x, t):
    ind = 0
    for i in range(len(x)):
        if x[i] > t:
            ind = i
            break

    return a[ind-1] + b[ind-1] * (t - x[ind]) + c[ind-1] * (t-x[ind]) ** 2 + d[ind-1] * (t-x[ind]) ** 3


def cube(x, y):
    h = [0] * len(x)
    l = [0] * len(x)
    for i in range(len(x)-1):
        h[i] = round(x[i + 1] - x[i], 3)
        l[i] = round((y[i + 1] - y[i]) / h[i], 3)
    delta = [0] * len(x)
    lamb = [0] * len(x)
    delta[0] = -0.5 * h[1] / (h[0] + h[1])
    lamb[0] = 1.5 * (l[1] - l[0]) / (h[1] + h[0])
    for i in range(2, len(x)):
        delta[i - 1] = - h[i] / (2 * h[i - 1] + 2 * h[i] + h[i - 1] * delta[i - 2])
    for i in range(2, len(x)):
        lamb[i - 1] = (2 * l[i] - 3 * l[i - 1] - h[i - 1] * lamb[i - 2])/(2 * h[i - 1] + 2 * h[i] + h[i - 1] * delta[i - 2])
    c = [0] * len(x)
    b = [0] * len(x)
    d = [0] * len(x)
    a = [0] * len(x)
    for i in range(len(x) - 1, 0, -1):
        c[i - 1] = round(delta[i - 1] * c[i] + lamb[i - 1], 3)
    a[:-1] = y[1:]
    for i in range(0, len(x) - 1):
        b[i] = round(l[i] + 2 / 3 * c[i] * h[i] + 1 / 3 * h[i] * c[i - 1], 3)
        d[i] = round((c[i] - c[i - 1]) / (3 * h[i]), 3)
    return a, b, c, d


x = [0.172, 0.567, 1.113, 2.119, 2.769]
y = [-7.057, -5.703, -0.132, 1.423, 2.832]

a, b, c, d = cube(x, y)


#a, b, c, d = cubic_approx(x, y)
print('a', a)
print('b', b)
print('c', c)
print('d', d)

#a, b, c, d = cube(x, y)

xnew = np.linspace(x[0], x[-1]-0.01, 1000)
ynew = [makeCub(a, b, c, d, x, i) for i in xnew]
xnew2 = np.linspace(x[0], x[-1], 100)
ynew2 = [lagran(x, y, i) for i in xnew2]

plt.plot(x, y, 'o', xnew, ynew, '-', xnew2, ynew2, '-')
plt.grid(True)
plt.show()