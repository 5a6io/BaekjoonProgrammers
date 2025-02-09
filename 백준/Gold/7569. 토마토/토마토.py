import sys
from collections import deque

input = sys.stdin.readline

# 1 -> 익은 토마토, 0 -> 익지 않은 토마토, -1 -> 빈 곳
M, N, H = map(int, input().split()) #M -> x, N -> y, H -> z
graph = []
for _ in range(H):
    box = []
    for _ in range(N):
        box.append(list(map(int, input().split())))
    graph.append(box)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
q = deque()

def bfs():
    day = 0
    while q:
        cx, cy, cz, d = q.popleft()

        for i in range(6):
            nx, ny, nz = cx + dx[i], cy + dy[i], cz + dz[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = 1
                    day = d + 1
                    q.append((nx, ny, nz, d + 1))

    return day

for z in range(H):
    for y in range(N):
        for x in range(M):
            if graph[z][y][x] == 1:
                q.append((x, y, z, 0))

res = bfs()

if any(graph[i][j][k] == 0 for i in range(H) for j in range(N) for k in range(M)):
    print(-1)
else:
    print(res)