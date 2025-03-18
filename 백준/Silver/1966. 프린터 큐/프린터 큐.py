import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    D = list(zip(list(map(int, input().split())), range(N)))
    q = deque(D)
    cnt = 1
    while q:
        mx = max(q)[0]
        d = q.popleft()
        if d[0] < mx:
            q.append(d)
        elif d[0] == mx:
            if d[1] == M:
                print(cnt)
                break
            else:
                cnt += 1