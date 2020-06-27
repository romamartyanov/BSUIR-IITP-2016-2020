import gauss
import numpy

Ax_B = numpy.array([[3.389, 0.273, 0.126, 0.418, 0.144],
                    [0.329, 2.796, 0.179, 0.278, 0.297],
                    [0.186, 0.275, 2.987, 0.316, 0.529],
                    [0.197, 0.219, 0.274, 3.127, 0.869]])

Ax = numpy.array([[3.389, 0.273, 0.126, 0.418],
                  [0.329, 2.796, 0.179, 0.278],
                  [0.186, 0.275, 2.987, 0.316],
                  [0.197, 0.219, 0.274, 3.127]])

_Ax = [[3.389, 0.273, 0.126, 0.418],
       [0.329, 2.796, 0.179, 0.278],
       [0.186, 0.275, 2.987, 0.316],
       [0.197, 0.219, 0.274, 3.127]]

B = numpy.array([0.144, 0.297, 0.529, 0.869])

print(Ax_B)
print("\n")

x = numpy.round(gauss.gauss_func(Ax_B), 3)
print("X:")
print(x)
print()

global Ax_inverse
try:
    Ax_inverse = numpy.round(numpy.linalg.inv(Ax), 3)

except numpy.linalg.LinAlgError:
    print("Обратную матрицу взять невозможно")

else:
    print("Обратная матрица:")
    print(Ax_inverse)
    print("\n")

Ax_det = numpy.linalg.det(Ax)
# print(Ax_det)
# print()

del_B = 0.001
del_X = numpy.linalg.norm(Ax_inverse) * del_B
print(del_B, del_X)
print()

sig_B = del_B / numpy.linalg.norm(B)
sig_X = numpy.linalg.norm(Ax) * numpy.linalg.norm(Ax_inverse) * sig_B
print(sig_B, sig_X)
print()


# def get_matrix_minor(m, i, j):
#     return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


                                           # x  y
# c11 = numpy.linalg.det(get_matrix_minor(_Ax, 0, 0)) / Ax_det
# print(c11)
# c12 = numpy.linalg.det(get_matrix_minor(_Ax, 1, 0)) / Ax_det
# print(c12)
# c13 = numpy.linalg.det(get_matrix_minor(_Ax, 2, 0)) / Ax_det
# print(c13)
# c14 = numpy.linalg.det(get_matrix_minor(_Ax, 3, 0)) / Ax_det
# print(c14)
# print()
#
# c21 = numpy.linalg.det(get_matrix_minor(_Ax, 0, 1)) / Ax_det
# print(c21)
# c22 = numpy.linalg.det(get_matrix_minor(_Ax, 1, 1)) / Ax_det
# print(c22)
# c23 = numpy.linalg.det(get_matrix_minor(_Ax, 2, 1)) / Ax_det
# print(c23)
# c24 = numpy.linalg.det(get_matrix_minor(_Ax, 3, 1)) / Ax_det
# print(c24)
# print()
#
# c31 = numpy.linalg.det(get_matrix_minor(_Ax, 0, 2)) / Ax_det
# print(c31)
# c32 = numpy.linalg.det(get_matrix_minor(_Ax, 1, 2)) / Ax_det
# print(c32)
# c33 = numpy.linalg.det(get_matrix_minor(_Ax, 2, 2)) / Ax_det
# print(c33)
# c34 = numpy.linalg.det(get_matrix_minor(_Ax, 3, 2)) / Ax_det
# print(c34)
# print()
#
# c41 = numpy.linalg.det(get_matrix_minor(_Ax, 0, 3)) / Ax_det
# print(c41)
# c42 = numpy.linalg.det(get_matrix_minor(_Ax, 1, 3)) / Ax_det
# print(c42)
# c43 = numpy.linalg.det(get_matrix_minor(_Ax, 2, 3)) / Ax_det
# print(c43)
# c44 = numpy.linalg.det(get_matrix_minor(_Ax, 3, 3)) / Ax_det
# print(c44)
# print()
