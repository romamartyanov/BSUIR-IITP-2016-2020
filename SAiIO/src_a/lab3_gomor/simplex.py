import numpy as np
from optimization import common


ITERATION_LIMIT = 10000


class Simplex:
    def __init__(self, A, c, x, J, b=None):
        self.A = np.array(A)
        self.c = c
        self.x = x
        self.b = b
        self.J = np.array(J) - 1

    def solve(self, mode='straight'):
        if mode == 'straight':
            return self.iterations(self.A, self.c, self.x, self.J)
        elif mode == 'dual':
            return self.iterations_dual(self.A, self.c, self.J, self.b)

    def find_optimal_plan(self):
        m, n = self.A.shape
        A_new = self.A

        for i, bi in enumerate(self.b):
            if bi < 0:
                self.b[i] *= -1
                A_new[i] = A_new[i] * -1
        print('AAAA', A_new)
        print(self.b)
        x = [0] * n + self.b
        c = [0] * n + [-1] * m
        J = list(range(n, n + m))
        print('x:', x)

        A_new = np.hstack((A_new, np.eye(m)))
        print(A_new)
        x_found, J_found = self.iterations(A_new, c, x, J)
        print(x_found, J_found)
        for xi in x_found[n:]:
            if xi != 0:
                print('Задача несовместна!')
                return
        
        A_base = A_new[:, J_found]

        print()
        print('A base:', A_base)
        n0 = n
        while True:
            J = list(range(n, n + m))
            print('J_range:', set(J))
            print('J_found', set(J_found))
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
                print('New J', J_found)
                break
        return A_new[:, :n0], J_found, x_found[:n0]

    def iterations(self, A, c, x, J, j0=None, s=None, Ab_prev=None, Ab_prev_inv=None, iteration=0):
        if iteration > ITERATION_LIMIT:
            raise OverflowError('Iterations limit reached')

        print('ITERATION #{}'.format(iteration))

        m = len(A)
        n = len(x)
        Ab = np.zeros((m, m))
        cb = []
        
        for i, j in enumerate(J):
            Ab[:, i] = A[:, j]
            cb.append(c[j])
        
        print()
        print('A basic:')
        print(Ab)

        if j0 == None:
            Ab_inv = np.linalg.inv(Ab)
        else:
            Ab_inv = common.get_row_inversed(Ab_prev, Ab_prev_inv, A[:, j0], s)
        u = np.dot(cb, Ab_inv)
        delta = np.dot(u, A) - c

        print(c, cb)
        print('A basic inversed:')
        print(Ab_inv)
        print('u: {}'.format(u))
        print('delta: {}'.format(delta))
    
        J_not_base = [i for i, t in enumerate(delta) if t < 0 and i not in J]

        is_optimal = True
        for i, xi in enumerate(delta):
            if i not in J and xi < 0:
                is_optimal = False
                break 

        if is_optimal:
            print('Optimal plan found')
            return x, J
        
        j0 = J_not_base[0]
        z = np.dot(Ab_inv, A[:, j0])
        print('z:', z)

        theta = []
        for i in range(m):
            if z[i] > 0:
                theta.append(x[J[i]] / z[i])
            else:
                theta.append(np.inf)
        
        lowest_theta = np.min(theta)

        print('Theta: {}'.format(theta))
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

        print('New vector J:', J)
        print('x #{} = {}'.format(iteration, x))
        print()
        return self.iterations(A, c, x, J, j0, lowest_theta_pos, Ab, Ab_inv, iteration + 1)
    
    def iterations_dual(self, A, c, J, b, y=None, iteration=0):
        if iteration > ITERATION_LIMIT:
            raise OverflowError('Iterations limit reached')

        print('ITERATION #{}'.format(iteration))

        m = len(A)
        n = len(c)
        Ab = np.zeros((m, m))
        cb = []
        
        print('J:', J)
        for i, j in enumerate(J):
            Ab[:, i] = A[:, j]
            cb.append(c[j])

        Ab_inv = np.linalg.inv(Ab)
        print()
        print('A basic:')
        print(Ab)

        
        if not iteration:
            y = np.dot(cb, Ab_inv)

        kappa = np.zeros(n)
        kappa_basic = np.dot(Ab_inv, b)
  
        kappa_neg = 0
        j_kappa = 0
        for i, kappa_val in enumerate(kappa_basic):
            kappa[J[i]] = kappa_val
            if kappa_val < 0:
                j_kappa = i
                kappa_neg = kappa_val
                #break
        
        if all(kappa_basic >= 0):
            print('GOOD:', kappa)
            return kappa

        delta_y = Ab_inv[j_kappa]

        print('kappa basic:', kappa_basic)
        print('selected kappa:', kappa_neg)
        print('position:', j_kappa)
        print('kappa:', kappa)
        print('dy\':', delta_y)

        #J_not_base = [x for x in np.arange(n) if x not in J]
        mu = np.zeros(n)

        for j in range(n):
            if j not in J:
                mu[j] = np.dot(delta_y, A[:, j])
        
        mu = np.array(mu)
        if all(mu >= 0):
            raise Exception('The problem is not feasible')

        print('mu:', mu)
        
        sigma = np.zeros(mu.shape)
        min_sigma = 10**10
        min_sigma_pos = 0

        for i, mu_val in enumerate(mu):
            if mu_val < 0:
                sigma[i] = (c[i] - np.dot(A[:, i], y)) / mu[i]
                if sigma[i] < min_sigma:
                    min_sigma = sigma[i]
                    min_sigma_pos = i

        print('sigma:', sigma)
        print('min sigma:', min_sigma)
        print('min sigma pos:', min_sigma_pos)

        J[j_kappa] = min_sigma_pos
        y = y + min_sigma * delta_y
        print('y:', y)

        return self.iterations_dual(A, c, J, b, y, iteration + 1)
