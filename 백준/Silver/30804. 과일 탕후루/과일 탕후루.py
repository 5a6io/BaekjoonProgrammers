import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input()) #  과일의 개수
S = list(map(int, input().split()))

fruit = defaultdict(int)
s, e, kind = 0, 0, 0
res = 0
while e < N:
    if fruit[S[e]] == 0:
        kind += 1
    fruit[S[e]] += 1

    while kind > 2:
        fruit[S[s]] -= 1
        if fruit[S[s]] == 0:
            kind -= 1
        s += 1

    res = max(res, e - s + 1)
    e += 1

print(res)