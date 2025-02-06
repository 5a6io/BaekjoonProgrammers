import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
res = [0] * T
for t in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1


    def bfs(x, y):
        q = deque()
        q.append((x, y))
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        while q:
            cx, cy = q.popleft()

            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx, ny))

        res[t] += 1

    for x in range(M):
        for y in range(N):
            if graph[x][y] == 1:
                bfs(x, y)

print(*res, sep='\n')