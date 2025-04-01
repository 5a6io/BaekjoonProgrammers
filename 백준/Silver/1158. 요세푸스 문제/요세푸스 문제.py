import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
q = deque([i for i in range(1, N+1)])

print('<', end='')
while q:
    for _ in range(K - 1):
        q.append(q.popleft())
    if len(q) - 1 > 0:
        print(q.popleft(), end=', ')
    else:
        print(q.popleft(), end='>')