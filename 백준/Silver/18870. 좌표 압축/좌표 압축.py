import sys

input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
S = sorted(list(set(X)))

res = {}
for i in range(len(S)):
    res[S[i]] = i

for x in X:
    print(res[x], end=' ')