import sys

input = sys.stdin.readline

N, M = map(int, input().split())
name = {}
num = {}
for i in range(1, N+1):
    n = input().strip()
    name[n] = i
    num[i] = n

for _ in range(M):
    q = input().strip()
    if q.isdigit():
        print(num[int(q)])
    else:
        print(name[q])