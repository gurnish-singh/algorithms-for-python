n, k = map(int, input().split())


def new_m(p, q):  # create a matrix filled with 0s
    matrix = [[1 for row in range(p + 1)] for col in range(q + 1)]
    return matrix


def bin2(n, k):
    B = new_m(k, n)
    for i in range(0, n):
        for j in range(0, k):
            if (j == 0) or (j == i):
                B[i][j] = 1
            else:
                B[i][j] = B[i - 1][j - 1] + B[i - 1][j]
    return B[n][k]


print(bin2(n, k))


