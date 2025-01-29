import sys

input = sys.stdin.readline

S = input().strip().split('-')

res = sum(list(map(int, S[0].split('+'))))
for i in range(1, len(S)):
    tmp = list(map(int, S[i].split('+')))
    res -= sum(tmp)

print(res)