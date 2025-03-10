import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
q = deque()
for y in range(n):
    for x in range(m):
        if board[y][x] == 2:
            q.append((y, x))
            board[y][x] = 0
            break

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]
while q:
    y, x = q.popleft()

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= ny < n and 0<= nx < m and not visited[ny][nx] and board[ny][nx] == 1:
            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))

for y in range(n):
    for x in range(m):
        if board[y][x] > 0 and not visited[y][x]:
            print(-1, end=' ')
        else:
            print(visited[y][x], end=' ')
    print()