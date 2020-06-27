from functools import reduce

import numpy as np

from src.dual_simplex.dual_task import DualTask


class NoPlanException(Exception):
    def __init__(self, message):
        super(NoPlanException, self).__init__(message)


class DualSimplex:
    def __init__(self, task: DualTask):
        self.A = task.A
        self.b = task.b
        self.c = task.c
        self.d_lo = task.d_lo
        self.d_hi = task.d_hi

        self.n, self.m = self.A.shape

    def iterations(self, A, c, x, J, j0=None, s=None, Ab_prev=None, Ab_prev_inv=None, iteration=0):
        if iteration > 10000:
            raise OverflowError('Iterations limit reached')

        # print('ITERATION #{}'.format(iteration))

        m = len(A)
        n = len(x)
        Ab = np.zeros((m, m))
        cb = []

        # print('n: {}, m: {}'.format(n, m))
        # print(Ab.shape, A.shape, len(J))
        for i, j in enumerate(J):
            Ab[:, i] = A[:, j]
            cb.append(c[j])

        # print()
        # print('A basic:')
        # print(Ab)

        Ab_inv = np.linalg.inv(Ab)
        u = np.dot(cb, Ab_inv)
        delta = np.dot(u, A) - c

        # print(c, cb)
        # print('A basic inversed:')
        # print(Ab_inv)
        # print('u: {}'.format(u))
        # print('delta: {}'.format(delta))

        J_not_base = [i for i, t in enumerate(delta) if t < 0 and i not in J]

        is_optimal = True
        for i, xi in enumerate(delta):
            if i not in J and xi < 0:
                is_optimal = False
                break

        if is_optimal:
            # print('Optimal plan found')
            return x, J

        j0 = J_not_base[0]
        z = np.dot(Ab_inv, A[:, j0])
        # print('z:', z)

        theta = []
        # print('J:', J)
        for i in range(m):
            if z[i] > 0:
                theta.append(x[J[i]] / z[i])
            else:
                theta.append(np.inf)

        lowest_theta = np.min(theta)

        # print('Theta: {}'.format(theta))
        if lowest_theta == np.inf:
            print('Function is not limited')
            return

        lowest_theta_pos = theta.index(lowest_theta)
        J[lowest_theta_pos] = j0

        x[j0] = lowest_theta
        for i in range(n):
            if i not in J:
                x[i] = 0
        for i, j in enumerate(J):
            if i != lowest_theta_pos:
                x[j] -= lowest_theta * z[i]

        # print('New vector J:', J)
        # print('x #{} = {}'.format(iteration, x))
        # print()
        return self.iterations(A, c, x, J, j0, lowest_theta_pos, Ab, Ab_inv, iteration + 1)

    def find_optimal_plan(self):
        m, n = self.A.shape
        A_new = self.A

        for i, bi in enumerate(self.b):
            if bi < 0:
                self.b[i] *= -1
                A_new[i] = A_new[i] * -1
        # print('AAAA', A_new)
        # print(self.b)
        x = [0] * n + self.b
        c = [0] * n + [-1] * m
        J = list(range(n, n + m))
        # print('x:', x)

        A_new = np.hstack((A_new, np.eye(m)))
        # print(A_new)
        x_found, J_found = self.iterations(A_new, c, x, J)
        # print(x_found, J_found)
        for xi in x_found[n:]:
            if xi != 0:
                print('Задача несовместна!')
                return

        A_base = A_new[:, J_found]

        # print()
        # print('A base:', A_base)
        n0 = n
        while True:
            J = list(range(n, n + m))
            # print('J_range:', set(J))
            # print('J_found', set(J_found))
            if len(set(J) & set(J_found)) == 0:
                break
            A_base = A_new[:, J_found]
            for k, artificial_id in enumerate(J):
                if artificial_id not in J_found:
                    continue

                success = False
                for not_base_id in range(n):
                    if not_base_id not in J_found:
                        l = np.dot(np.linalg.inv(A_base), A_new[:, not_base_id])
                        if l[k] != 0:
                            J_found[J_found.index(artificial_id)] = not_base_id
                            success = True
                            break

                if not success:
                    i = artificial_id - n
                    J_found.remove(artificial_id)
                    m -= 1

                    for idd, j in enumerate(J_found):
                        if j > artificial_id:
                            J_found[idd] -= 1
                    A_new = np.delete(A_new, i, axis=0)
                    A_new = np.delete(A_new, artificial_id, axis=1)
                # print('New J', J_found)
                break
        return A_new[:, :n0], J_found, x_found[:n0]

    def solve(self, J=None):
        if J is None:
            _, J, _ = self.find_optimal_plan()  # choices(range(self.m), k=self.n)
        A_b = self.A[:, J]
        c_b = np.array(self.c)[J]

        B = np.linalg.inv(A_b)

        y = np.dot(c_b, B)
        delta = np.dot(y, self.A) - self.c

        J_n = [i for i in range(self.m) if i not in J]
        J_nn = [j for j in J_n if delta[j] < 0]
        J_np = [j for j in J_n if delta[j] >= 0]

        return self.__solve(J, J_n, J_nn, J_np, delta, B)

    def __build_N(self, J, B, J_n, J_np):
        N = np.zeros(self.m)
        N[J_n] = [self.d_lo[j] if j in J_np else self.d_hi[j] for j in J_n]

        AjNj = reduce(lambda a, b: a + b, [self.A[:, j] * N[j] for j in J_n])
        # print('sum of Aj*Nj:', AjNj)
        # print('b - sum =', self.b - AjNj)
        N[J] = np.dot(B, self.b - AjNj)

        return N

    def __is_optimal(self, N, J):
        optimal = True
        jk = 0
        for i, n in enumerate(N):
            if i not in J: continue
            if not self.d_lo[i] <= N[i] <= self.d_hi[i]:
                optimal = False
                jk = i
                break

        return optimal, jk

    def __solve(self, J, J_n, J_nn, J_np, delta, B, iteration=0):
        # print()
        # print('#' * 20)
        # print('Iteration #{}'.format(iteration))
        # print('delta =', delta)
        # print('J_nn:', J_nn)
        # print('J_np:', J_np)

        # print('B:', B)
        N = self.__build_N(J, B, J_n, J_np)
        # print('N:', N)

        optimal, jk = self.__is_optimal(N, J)

        if optimal:
            # print('Ans: ', N, np.dot(self.c, N))
            return N, J, np.dot(self.c, N)

        k = J.index(jk)
        # print('jk =', jk, 'k =', k)
        mu_jk = 1 if N[jk] < self.d_lo[jk] else -1  # 1 если меньше минимального, -1 если больше максимального

        dy = mu_jk * B[k]
        # print('dy =', dy)

        mu = np.dot(dy, self.A)
        mu[jk] = mu_jk
        # print('mu =', mu)

        sigma = {}
        for j in J_n:
            if j in J_np and mu[j] < 0 or j in J_nn and mu[j] > 0:
                # print('j = {} mu[j] = {}, delta[j] = {}'.format(j, mu[j], delta[j]))
                sigma[j] = -delta[j] / mu[j]
            else:
                sigma[j] = np.inf

        sigma0 = np.inf
        js = 0
        for k, v in sigma.items():
            if v < sigma0:
                sigma0 = v
                js = k

        if sigma0 == np.inf:
            raise NoPlanException("Нет допустимых планов")
        # print('sigma =', sigma)

        delta_new = delta + sigma0 * mu
        # print('new delta =', delta_new)

        J[J.index(jk)] = js
        # print('New J:', J)
        B = np.linalg.inv(self.A[:, J])

        if mu[jk] == 1 and js in J_np:
            J_np[J_np.index(js)] = jk
        elif mu[jk] == -1 and js in J_np:
            J_np.remove(js)
        elif mu[jk] == 1 and js not in J_np:
            J_np.append(jk)
        elif mu[jk] == -1 and js not in J_np:
            pass

        J_n = [i for i in range(self.m) if i not in J]
        J_nn = [j for j in J_n if j not in J_np]
        # print(J_np, J_nn)

        return self.__solve(J, J_n, J_nn, J_np, delta_new, B, iteration + 1)
