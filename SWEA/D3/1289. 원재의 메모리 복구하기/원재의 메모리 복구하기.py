T = int(input())

for tc in range(1, T+1):
    bit = list(input())
    n = len(bit)

    find = [0] * n
    res = 0

    for i in range(n):
        if find[i] != int(bit[i]):
            for j in range(i, n):
                find[j] = int(bit[i])
            res += 1

    print(f"#{tc} {res}")