import sys

input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
S = sorted(list(set(X)))

res = dict(zip(S, range(len(S))))

for x in X:
    print(res[x], end=' ')