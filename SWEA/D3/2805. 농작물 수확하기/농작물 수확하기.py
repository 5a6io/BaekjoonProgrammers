t = int(input())
for i in range(1, t + 1):
    n = int(input())
    farm = [list(map(int, input().strip())) for _ in range(n)]

    if n == 1:
        print(f"#{i} {farm[0][0]}")

    else:
        res = 0
        mid = n//2
        for j in range(mid):
            res += sum(farm[j][mid - j:mid + j + 1])

        for j in range(mid, n):
            res += sum(farm[j][j - mid:n - j + mid])

        print(f"#{i} {res}")