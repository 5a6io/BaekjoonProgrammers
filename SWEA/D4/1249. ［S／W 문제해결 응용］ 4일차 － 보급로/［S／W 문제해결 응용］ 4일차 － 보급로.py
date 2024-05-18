import math
from collections import deque

T = int(input())
INF = math.inf

for test_case in range(1, T+1):
    n = int(input())
    maze = [list(map(int, list(input()))) for _ in range(n)]
    moveDir = [[1, 0], [-1, 0], [0, -1], [0, 1]]  # 상, 하, 좌, 우
    visited = [[INF for _ in range(n)] for _ in range(n)]

    road = deque()
    road.append((0, 1, maze[0][1]))
    road.append((1, 0, maze[1][0]))


    while road:
        nx, ny, time = road.popleft()

        for i in range(4):
            x = nx + moveDir[i][0]
            y = ny + moveDir[i][1]

            if x < 0 or n <= x or y < 0 or n <= y or (x, y) == (0, 0) or visited[x][y] <= maze[x][y] + time:
                continue

            visited[x][y] = time + maze[x][y]
            road.append((x, y, visited[x][y]))

    print(f"#{test_case} {visited[-1][-1]}")
