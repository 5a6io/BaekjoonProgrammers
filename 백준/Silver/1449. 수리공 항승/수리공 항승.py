import sys

input = sys.stdin.readline

n, l = map(int, input().split())
lack = list(map(int, input().split()))
lack.sort()
blocked = [False]*n

s = lack[0] - 0.5
e = s + l
res = 1
for i in range(n):
    if s < lack[i] < e:
        continue
    else:
        res += 1
        s = lack[i] - 0.5
        e = s + l

print(res)