import math
import numpy

n = 4


T = numpy.zeros((n, n))
X = numpy.zeros(n)
Y = numpy.zeros(n)


Ax_B = numpy.array([[3.389, 0.273, 0.126, 0.418, 0.144],
                    [0.329, 2.796, 0.179, 0.278, 0.297],
                    [0.186, 0.275, 2.987, 0.316, 0.529],
                    [0.197, 0.219, 0.274, 3.127, 0.869]])

A = numpy.array([[3.389, 0.273, 0.126, 0.418],
                  [0.329, 2.796, 0.179, 0.278],
                  [0.186, 0.275, 2.987, 0.316],
                  [0.197, 0.219, 0.274, 3.127]])

A_t = A.transpose()

S = numpy.dot(A.T, A)

print('S: \n', S)

B = numpy.array([0.144, 0.297, 0.529, 0.869])


print('Метод квадратного корня:')
print('A: ', A, '\n')
print('B: ', B, '\n')

A_det = numpy.linalg.det(A)


T[0][0] = math.sqrt(S[0][0])

for j in range(n - 1):
    j = j + 1
    # T[j][0] = round(A[j][0] / T[0][0], 1)
    T[j][0] = S[j][0] / T[0][0]

print(T, '\n')


for i in range(n):
    if i > 0:
        temp = 0
        for k in range(i - 1):
            temp += T[i][k]**2

        # T[i][i] = round(math.sqrt(A[i][i] - temp), 1)
        T[i][i] = math.sqrt(S[i][i] - temp)


print(T, '\n')


for i in range(n):
    for j in range(n):
        if i < j:

            temp = 0
            for k in range(i):
                temp += T[i][k] * T[j][k]

            # T[j][i] = round((A[j][i] - temp) / T[i][i], 1)
            T[j][i] = (S[j][i] - temp) / T[i][i]

        if i > j:
            T[j][i] = 0

print(T, '\n')


for i in range(n):
    if i > 0:
        temp = 0
        for k in range(i):

            temp += T[i][k]**2

        # T[i][i] = round(math.sqrt(A[i][i] - temp), 1)
        T[i][i] = math.sqrt(A[i][i] - temp)


print('T: ', '\n', T, '\n')

T_transpose = T.transpose()
print('T_transpose: ', '\n', T_transpose, '\n')


Y[0] = B[0] / T[0][0]

for i in range(n):
    if i > 0:
        temp = 0

        for k in range(i):
            temp += T[i][k] * Y[k]

        # Y[i] = round((B[i] - temp) / T[i][i], 1)
        Y[i] = (B[i] - temp) / T[i][i]


print('Y:', Y, '\n')


# X[n - 1] = round(Y[n - 1] / T[n - 1][n - 1], 1)
X[n - 1] = Y[n - 1] / T[n - 1][n - 1]

i = n - 2
while i >= 0:
    k = i + 1
    temp = 0

    while k < n:
        temp += T[k][i] * X[k]
        k = k + 1

    X[i] = (Y[i] - temp) / T[i][i]

    i = i - 1


print('X:', X)

print()
print('==============')
print()

Ax_B = numpy.matrix([[3.389, 0.273, 0.126, 0.418, 0.144],
                    [0.329, 2.796, 0.179, 0.278, 0.297],
                    [0.186, 0.275, 2.987, 0.316, 0.529],
                    [0.197, 0.219, 0.274, 3.127, 0.869]])

A = numpy.matrix([[3.389, 0.273, 0.126, 0.418],
                  [0.329, 2.796, 0.179, 0.278],
                  [0.186, 0.275, 2.987, 0.316],
                  [0.197, 0.219, 0.274, 3.127]])


B = numpy.matrix([0.144, 0.297, 0.529, 0.869])

print('A:', '\n', A)
print()

print('Сопраженная матраца для A:')

A_conjugate = A.getH()
print(A_conjugate)
print()

print('Симметризация матрицы A:')
A_symmetric_my = 0.5 * (A + A_conjugate)

print(A_symmetric_my)

print()
print('==============')
print()

print("Определитель матрицы А: ", A_det, 'или', T[0][0]**2 * T[1][1]**2 * T[2][2]**2 * T[3][3]**2)

print()
print('==============')
print()

null_matrix = numpy.identity(4)

x = []


for i in range(4):
    y = numpy.linalg.solve(T, null_matrix[i])

    print(y)

    x.append(numpy.linalg.solve(T_transpose, y))

print()
x = numpy.transpose(numpy.array(x).round(3))
print(x, '\nили')

A_inverse = numpy.round(numpy.linalg.inv(A), 3)
print(A_inverse)