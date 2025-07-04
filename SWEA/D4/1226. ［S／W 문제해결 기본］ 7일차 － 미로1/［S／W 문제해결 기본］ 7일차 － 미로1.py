from collections import deque

for tc in range(10):
    case = int(input())
    board = [list(input()) for _ in range(16)]
    visit = [[False for _ in range(16)] for _ in range(16)]
    q = deque()
    q.append((1, 1))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        cy, cx = q.popleft()
        if board[cy][cx] == "3":
            print(f"#{case} 1")
            break

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 < ny < 16 and 0 < nx < 16:
                if not visit[ny][nx]:
                    if board[ny][nx] == "0" or board[ny][nx] == "3":
                        visit[ny][nx] = True
                        q.append((ny, nx))
    else:
        print(f"#{case} 0")