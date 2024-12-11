import sys

input = sys.stdin.readline
ts = int(input())
coins = [25, 10, 5, 1]

for t in range(ts):
    c = int(input())
    res = []
    for coin in coins:
        if c < coin:
            res.append(0)
            continue
        div, c = divmod(c, coin)
        res.append(div)

    print(*res, sep=' ')