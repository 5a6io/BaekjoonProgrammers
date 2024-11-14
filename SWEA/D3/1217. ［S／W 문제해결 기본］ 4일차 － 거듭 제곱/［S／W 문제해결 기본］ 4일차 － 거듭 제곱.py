def involution(n, m):
    if m == 0:
        return 1
    if m == 1:
        return n

    return involution(n, m - 1) * n


for i in range(10):
    t = int(input())
    n, m = map(int, input().split())

    print(f"#{t} {involution(n, m)}")