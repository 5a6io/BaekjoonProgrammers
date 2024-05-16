def multiply(a, b):
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j] % 1000
    return c


def squared(A, B):
    if B == 1:
        return A
    
    tmp = squared(A, B//2)
    if B % 2 == 0:
        return multiply(tmp, tmp)
    else:
        return multiply(multiply(tmp, tmp), A)


n, b = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
C = squared(A, b)
for i in range(n):
    for j in range(n):
        C[i][j] %= 1000

for i in C:
    print(*i)