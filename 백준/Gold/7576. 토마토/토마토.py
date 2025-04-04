import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(m)]
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
q = deque()

for i in range(m):
    for j in range(n):
        if boxes[i][j] == 1:
            q.append((i, j, 0))

def bfs():
    res = 0
    while q:
        y, x, day = q.popleft()
        for d in dir:
            ny, nx = y + d[0], x + d[1]
            if 0 <= ny < m and 0 <= nx < n:
                if boxes[ny][nx] == 0:
                    boxes[ny][nx] = 1
                    q.append((ny, nx, day + 1))
                    res = max(res, day + 1)

    for i in range(m):
        for j in range(n):
            if boxes[i][j] == 0:
                return -1

    return res


print(bfs())