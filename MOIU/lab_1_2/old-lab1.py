import numpy as np

a = np.array([[1., 0., 4.],
              [2., 1., 6.],
              [3., 4., 0.]], dtype=float)

a_minus1 = np.array([[-24., 20., -5.],
                     [18., -15., 4.],
                     [5., - 4., 1.]], dtype=float)

x = np.array([2., 2., 2.])

a_line = np.array([[1., 2., 5.],
                   [2., 2., 6.],
                   [3., 2., 0.]], dtype=float)

i = 1

# n_1
l = np.dot(a_minus1, x)
if l[i] == 0:
    print("neobratima")
    exit()

else:
    print('obratima')
# n_2
l_new = np.copy(l)
l_new[i] = -1

# n_3
l_new_new = np.dot((-1 / l[i]), l_new)

# n_4
E_n = np.eye(3, 3)
Q = np.copy(E_n)

for j in range(3):
    Q[j][i] = l_new_new[j]

# n_5
a_new = np.dot(Q, a_minus1)

print(a_new)
