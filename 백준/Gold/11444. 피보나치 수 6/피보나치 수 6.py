import sys
input = sys.stdin.readline


def multiply(a, b):
    n = len(a)
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= 1000000007
    return c


def squared(A, n):
    if n == 1:
        return A

    tmp = squared(A, n // 2)
    if n % 2 == 0:
        return multiply(tmp, tmp)
    else:
        return multiply(multiply(tmp, tmp), A)


n = int(input())
A = [[1, 1],
     [1, 0]]
print(squared(A, n)[0][1])