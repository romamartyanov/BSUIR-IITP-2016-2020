from lab_7.lib import solve


def test_1():
    B_f = [[2, 1, 0, 4, 0, 3, 0, 0],
           [0, 4, 0, 3, 1, 1, 3, 2],
           [1, 3, 0, 5, 0, 4, 0, 4]]
    c_f = [-1, -1, -1, -1, -2, 0, -2, -3]

    B = []
    B.append([
        [0, 0, 0.5, 2.5, 1, 0, -2.5, -2],
        [0.5, 0.5, -0.5, 0, 0.5, -0.5, -0.5, -0.5],
        [0.5, 0.5, 0.5, 0, 0.5, 1, 2.5, 4]
    ])
    B.append([
        [1, 2, -1.5, 3, -2.5, 0, -1, -0.5],
        [-1.5, -0.5, -1, 2.5, 3.5, 3, -1.5, -0.5],
        [1.5, 2.5, 1, 1, 2.5, 1.5, 3, 0]
    ])
    B.append([
        [0.75, 0.5, -1, 0.25, 0.25, 0, 0.25, 0.75],
        [-1, 1, 1, 0.75, 0.75, 0.5, 1, -0.75],
        [0.5, -0.25, 0.5, 0.75, 0.5, 1.25, -0.75, -0.25]
    ])
    B.append([
        [1.5, -1.5, -1.5, 2, 1.5, 0, 0.5, -1.5],
        [-0.5, -2.5, -0.5, -1, -2.5, 2.5, 1, 2],
        [-2.5, 1, -2, -1.5, -2.5, 0.5, 2.5, -2.5]
    ])
    B.append([
        [1, 0.25, -0.5, 1.25, 1.25, -0.5, 0.25, -0.75],
        [-1, -0.75, -0.75, 0.5, -0.25, 1.25, 0.25, -0.5],
        [0, 0.75, 0.5, -0.5, -1, 1, -1, 1]
    ])
    c = [
        [0, 60, 80, 0, 0, 0, 40, 0],
        [2, 0, 3, 0, 2, 0, 3, 0],
        [0, 0, 80, 0, 0, 0, 0, 0],
        [0, -2, 1, 2, 0, 0, -2, 1],
        [-4, -2, 6, 0, 4, -2, 60, 2]
    ]
    a = [-51.75, -436.75, -33.7813, -303.3750, -41.75]
    x_til = [1, 0, 0, 2, 4, 2, 0, 0]

    # x with krishka(shapka)
    x_kr = [0, 0, 0, 0, 0, 0, 0, 0]

    solve(B_f, c_f, B, c, a, x_til, x_kr)


if __name__ == "__main__":
    test_1()
