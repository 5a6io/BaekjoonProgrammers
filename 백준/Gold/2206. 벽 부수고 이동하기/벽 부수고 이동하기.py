import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        cy, cx, crack = q.popleft()

        if (cy, cx) == (N-1, M-1):
            return visited[cy][cx][crack]

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx][crack] and graph[ny][nx] == "0":
                    visited[ny][nx][crack] = visited[cy][cx][crack] + 1
                    q.append((ny, nx, crack))

                if graph[ny][nx] == "1" and crack == 0:
                    visited[ny][nx][1] = visited[cy][cx][0] + 1
                    q.append((ny, nx, 1))

    return -1

print(bfs())