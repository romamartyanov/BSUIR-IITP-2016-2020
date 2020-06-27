def main():
    x_set = [0.172, 0.567, 1.113, 2.119, 2.769]
    y_set = [-7.057, -5.703, -0.132, 1.423, 2.832]
    print("Разделенные разности")
    kdiff(x_set, y_set, len(y_set), 0)


def kdiff(x_set, y_set, set_len, k):
    new_yset = []
    if set_len == 1:
        return y_set

    for i in range(set_len - 1):
        n = (y_set[i+1]-y_set[i])/(x_set[i + k + 1]-x_set[i])
        new_yset.append(n)
    print(new_yset)
    k += 1
    kdiff(x_set, new_yset, len(new_yset),k)


if __name__ == "__main__":
    main()