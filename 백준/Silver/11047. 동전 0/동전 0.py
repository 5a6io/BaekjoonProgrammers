import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))
A.sort(reverse=True)

cnt = 0
for a in A:
    if a > K:
        continue
    else:
        cnt += (K//a)
        K %= a

print(cnt)