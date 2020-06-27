import numpy
import copy


def gauss_func(a):
    eps = 1e-16

    a = numpy.array(a)

    len_ox = len(a[:, 0])
    len_oy = len(a[0, :])

    for g in range(len_ox):

        max_in_a = abs(a[g][g])
        my = g
        t1 = g

        while t1 < len_ox:
            if abs(a[t1][g]) > max_in_a:
                max_in_a = abs(a[t1][g])
                my = t1
            t1 += 1

        if abs(max_in_a) < eps:
            raise DeterminateException("Check determinant")

        if my != g:
            b = copy.deepcopy(a[g])
            a[g] = copy.deepcopy(a[my])
            a[my] = copy.deepcopy(b)

        a_main = float(a[g][g])

        z = g
        while z < len_oy:
            a[g][z] = a[g][z] / a_main
            z += 1

        j = g + 1

        while j < len_ox:
            b = a[j][g]
            z = g

            while z < len_oy:
                a[j][z] = a[j][z] - a[g][z] * b
                z += 1
            j += 1

    a = back_trace(a, len_ox, len_oy)
    return a


class DeterminateException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def back_trace(a, len1, len2):
    a = numpy.array(a)
    i = len1 - 1
    while i > 0:
        j = i - 1

        while j >= 0:
            a[j][len1] = a[j][len1] - a[j][i] * a[i][len1]
            j -= 1
        i -= 1
    return a[:, len2 - 1]
