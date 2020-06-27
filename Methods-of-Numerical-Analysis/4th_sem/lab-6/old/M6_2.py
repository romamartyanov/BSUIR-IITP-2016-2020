def main():
    #x_set = [0.172, 0.567, 1.113, 2.119, 2.769]
    y_set = [-7.057, -5.703, -0.132, 1.423, 2.832]
    print("Конечные разности")
    kdiff(y_set, len(y_set))


def kdiff(y_set, set_len):
    new_set = []
    if set_len == 1:
        return y_set

    for i in range(set_len - 1):
        new_set.append(y_set[i + 1] - y_set[i])
    print(new_set)

    kdiff(new_set, len(new_set))


if __name__ == "__main__":
    main()