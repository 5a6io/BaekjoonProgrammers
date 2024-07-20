n, m = map(int, input().split())
cards = list(map(int, input().split()))

res = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if i != j and j != k and i != k:
                if res < cards[i]+cards[j]+cards[k] <= m:
                    res = cards[i]+cards[j]+cards[k]

print(res)