import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
draw = [list(input().rstrip()) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
rg_visited = [[False for _ in range(N)] for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x, color):
    global res
    q = deque([(y, x)])
    visited[y][x] = True

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx  + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx] and draw[ny][nx] == color:
                        visited[ny][nx] = True
                        q.append((ny, nx))

    res += 1

def rg_bfs(y, x, color):
    global rg
    q = deque([(y, x)])
    rg_visited[y][x] = True

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if 0 <= ny < N and 0 <= nx < N and not rg_visited[ny][nx]:
                if draw[ny][nx] == color:
                    rg_visited[ny][nx] = True
                    q.append((ny, nx))
                elif (draw[ny][nx] == 'R' and color == 'G') or (draw[ny][nx] == 'G' and color == 'R'):
                    rg_visited[ny][nx] = True
                    q.append((ny, nx))

    rg += 1

res = 0
rg = 0
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            bfs(y, x, draw[y][x])
        if not rg_visited[y][x]:
            rg_bfs(y, x, draw[y][x])

print(res, rg)