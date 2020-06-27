import numpy as np


def extend(a, b, c):
    a_extended = np.array(a)
    b_extended = np.array(b)
    c_extended = np.array(c)

    sa = sum(a)
    sb = sum(b)
    print(c_extended.shape, np.zeros((len(a), 1)))
    if sa > sb:
        b_extended = np.append(b_extended, sa - sb)
        c_extended = np.hstack((c_extended, np.zeros((len(a), 1))))
    else:
        a_extended = np.append(a_extended, sb - sa)
        c_extended = np.vstack((c_extended, np.zeros(len(b))))
    return a_extended, b_extended, c_extended


def build_X_north_west(a, b):
    m = len(a)
    n = len(b)
    x = np.zeros((m, n))
    J = []

    cur_a = np.copy(a)
    cur_b = np.copy(b)
    i, j = 0, 0
    while i < m:
        while j < n:
            min_val = min(cur_a[i], cur_b[j])
            x[i][j] = min_val
            cur_a[i] -= min_val
            cur_b[j] -= min_val
            J.append((i, j))
            if not cur_a[i]:
                i += 1
                break
            j += 1

    return x, J


def get_potentials(x, c, J):
    m, n = np.shape(x)

    a = np.zeros((m + n, m + n))
    b = np.zeros(m + n)

    k = 1
    for i, j in J:
        print('u[{}] + v[{}] = {}'.format(i, j, c[i][j]))

        a[k][i] = 1
        a[k][j + m] = 1
        b[k] = c[i][j]
        k += 1

    a[0][0] = 1
    print(a)
    res = np.linalg.solve(a, b)
    print('SOLVE: ', res)

    u = res[:m]
    v = res[m:]
    return u, v


def check_potentials(c, u, v, J):
    max_val = -10 ** 10
    max_val_pos = (-1, -1)
    for i, u_val in enumerate(u):
        for j, v_val in enumerate(v):
            if (i, j) not in J and u_val + v_val > c[i][j] and u_val + v_val - c[i][j] > max_val:
                max_val = u_val + v_val - c[i][j]
                max_val_pos = (i, j)
    print('Max potential diff:', max_val)
    return max_val_pos


def build_tree(x, J):
    m, n = np.shape(x)
    g = [[] for _ in range(m * n)]

    for i in range(m):
        for j in range(n):
            if (i, j) not in J:
                continue
            for k in range(j + 1, n):
                if (i, k) in J:
                    g[n * i + j].append(n * i + k)
                    g[n * i + k].append(n * i + j)
                    break
            for k in range(i + 1, m):
                if (k, j) in J:
                    g[n * i + j].append(n * k + j)
                    g[n * k + j].append(n * i + j)
                    break

    print(g)
    return g


def find_nearest(i, j, J):
    row = [pos for pos in J if pos[0] == i and pos[1] != j]
    col = [pos for pos in J if pos[1] == j and pos[0] != i]

    min_row_dist = 10 ** 10
    nearest_row_pos = (i, j)
    for row_pos in row:
        if abs(row_pos[1] - j) < min_row_dist:
            min_row_dist = abs(row_pos[1] - j)
            nearest_row_pos = row_pos

    min_col_dist = 10 ** 10
    nearest_col_pos = (i, j)
    for col_pos in col:
        if abs(col_pos[0] - i) < min_col_dist:
            min_col_dist = abs(col_pos[0] - i)
            nearest_col_pos = col_pos

    return nearest_row_pos, nearest_col_pos


def find_path(g, nearest_row_pos, nearest_col_pos, size):
    m, n = size

    def bfs(v, to):
        q = []
        q.append(v)
        used = [False for _ in range(m * n)]
        p = [0 for _ in range(m * n)]
        d = [0 for _ in range(m * n)]
        p[v] = -1

        print('v: {}, to: {}'.format(v, to))
        used[v] = True

        while len(q):
            v = q[-1]
            q.pop()
            for x in g[v]:
                if used[x]:
                    continue
                used[x] = True
                q.append(x)
                d[x] = d[v] + 1
                p[x] = v

        path = []
        v = to
        while v != -1:
            path.append(v)
            v = p[v]

        return path

    start = nearest_row_pos[0] * n + nearest_row_pos[1]
    end = nearest_col_pos[0] * n + nearest_col_pos[1]

    # from start to end
    path = bfs(start, end)
    print('path:', path)
    return path


def get_side_path_positions(path):
    k = 0
    new_path = []
    while k < len(path):
        pos = path[k]

        while k < len(path) and path[k][0] == pos[0]:
            k += 1

        if k < len(path):
            pos = path[k]
            new_path.append(path[k - 1])

        while k < len(path) and path[k][1] == pos[1]:
            k += 1
        if k < len(path):
            new_path.append(path[k - 1])

        if k >= len(path) and not \
                (path[-1][0] == path[-2][0] and path[-1][0] == path[0][0] or \
                 path[-1][1] == path[-2][1] and path[-1][1] == path[0][1]):
            new_path.append(path[-1])
            break
    return new_path


def update_path(x, path, J, new_pos):
    m, n = np.shape(x)
    x_new = np.copy(x)

    # return flat coordinates back to 2D
    path_extended = [(pos // n, pos - n * (pos // n)) for pos in path]

    path_extended = [new_pos] + path_extended
    print('\nPath extended:', path_extended)
    side_path = get_side_path_positions(path_extended)
    path_extended = side_path
    print('New path:', side_path)
    print()
    odd_positions = []
    for i in range(1, len(path_extended) // 2 + 1, 2):
        odd_positions.append(path_extended[i])
        if len(path) - i != i:
            odd_positions.append(path_extended[-i])
    # odd_positions = path_extended[1::2]
    print('Odd positions:', odd_positions)

    min_odd_pos_val = 10 ** 10
    min_odd_pos = (-1, -1)

    for i, j in odd_positions:
        # print(i, j, x[i][j])
        if x[i][j] < min_odd_pos_val:
            min_odd_pos_val = x[i][j]
            min_odd_pos = (i, j)

    print('Min odd pos value:', min_odd_pos_val)

    for i, j in path_extended:
        # print((i, j), (i, j) in odd_positions)
        if (i, j) in odd_positions:
            x_new[i][j] -= min_odd_pos_val
        else:
            x_new[i][j] += min_odd_pos_val

    J_new = []
    for i, j in J:
        if (i, j) != min_odd_pos:
            J_new.append((i, j))

    J_new.append(new_pos)
    return x_new, J_new


def iterations(x, J, c, iteration=0):
    if iteration == 100:
        raise OverflowError('Iteration limit reached')

    print('\nITERATION #{}\n'.format(iteration))
    m, n = np.shape(c)
    u, v = get_potentials(x, c, J)
    print(u, v)

    new_i, new_j = check_potentials(c, u, v, J)
    if new_i == -1 and new_j == -1:
        print('Soluition found: \nx = {}, \nJ = {}'.format(x, J))
        return x, J

    print('next:', new_i, new_j)
    tree = build_tree(x, J)
    nearest_row_pos, nearest_col_pos = find_nearest(new_i, new_j, J)
    print(nearest_row_pos, nearest_col_pos)
    path = find_path(tree, nearest_row_pos, nearest_col_pos, (m, n))
    print('Path:', path)
    x, J = update_path(x, path, J, (new_i, new_j))
    print('New x: {}, new J: {}'.format(x, J))
    return iterations(x, J, c, iteration + 1)


# matrix transport problem
def solve_mtp(a, b, c):
    if sum(a) != sum(b):
        a, b, c = extend(a, b, c)
    x, J = build_X_north_west(a, b)
    print('North west method returned: \nx = {}, \nJ = {}'.format(x, J))
    x, J = iterations(x, J, c)
    s = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            s += x[i][j] * c[i][j]
    print(c)
    print(s)
    return x, J
