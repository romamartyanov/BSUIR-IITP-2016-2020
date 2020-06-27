def main():
    x_set = [0.172, 0.567, 1.113, 2.119, 2.769]
    y_set = [-7.057, -5.703, -0.132, 1.423, 2.832]
    newts = []
    newts = kdiff(x_set, y_set, len(y_set), 0, newts)
    newton(1.68, x_set, y_set, newts)


def kdiff(x_set, y_set, set_len, k, newton_set):
    new_yset = []
    if set_len == 1:
        return newton_set

    for i in range(set_len - 1):
        n = (y_set[i+1]-y_set[i])/(x_set[i + k + 1]-x_set[i])
        new_yset.append(n)
    #print(new_yset)
    newton_set.append(new_yset[0])
    k += 1
    newton_set = kdiff(x_set, new_yset, len(new_yset),k, newton_set)
    return newton_set


def newton(x, x_set, y_set, newton_s):
    Nx = y_set[0]
    for i in range(len(newton_s)):
        temp = newton_s[i]
        for j in range(i+1):
            temp *= x - x_set[j]
        Nx += temp
    print("N4(x):", Nx)


if __name__ == "__main__":
    main()