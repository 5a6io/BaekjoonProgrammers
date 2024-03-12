from collections import deque

def solution(maps):
    move = [[0, 1], [0, -1], [-1, 0], [1, 0]]

    queue = deque()
    queue.append((0, 0))

    while queue:
        curX, curY = queue.popleft()

        for dx, dy in move:
            x = curX + dx
            y = curY + dy

            if 0 <= x < len(maps) and 0 <= y < len(maps[0]) and maps[x][y] == 1:
                maps[x][y] = maps[curX][curY] + 1
                queue.append((x, y))

    answer = maps[len(maps) - 1][len(maps[0]) - 1]

    if answer == 1:
        return -1
    else:
        return answer