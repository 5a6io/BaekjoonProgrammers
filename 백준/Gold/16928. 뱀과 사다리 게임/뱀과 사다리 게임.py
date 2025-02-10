import sys
from collections import deque

input = sys.stdin.readline

# 1 -> 100 도착 목표
N, M = map(int, input().split()) # N -> 사다리 수, M -> 뱀 수
ladders = {}
for _ in range(N):
    x, y = map(int, input().split())
    ladders[x] = y
snakes = {}
for _ in range(M):
    x, y = map(int, input().split())
    snakes[x] = y

visited = [0] * 101
visited[1] = 1
q = deque()
q.append(1)
cnt = 0
flag = True
while flag:
    l = len(q)
    for _ in range(l):
        cur = q.popleft()
        if cur == 100:
            print(cnt)
            flag = False
            break

        for i in range(1, 7):
            nx = cur + i
            if nx <= 100 and not visited[nx]:
                visited[nx] = 1
                if nx in ladders.keys():
                    visited[ladders[nx]] = 1
                    q.append(ladders[nx])
                elif nx in snakes.keys():
                    visited[snakes[nx]] = 1
                    q.append(snakes[nx])
                else:
                    q.append(nx)

    cnt += 1