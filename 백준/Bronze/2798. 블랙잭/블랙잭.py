n, m = map(int, input().split())
cards = list(map(int, input().split()))

res = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and i != k:
                if res < cards[i]+cards[j]+cards[k] <= m:
                    res = cards[i]+cards[j]+cards[k]

print(res)