import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
mx = max(map(max, board))

def backtracking(pos, cnt, res):
    global ans
    if res + (4-cnt) * mx <= ans:
        return

    if cnt == 4:
        ans = max(res, ans)
        return

    for y, x in pos:
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                visited[ny][nx] = 1
                backtracking(pos + [(ny, nx)], cnt + 1, res + board[ny][nx])
                visited[ny][nx] = 0

ans = 0
for y in range(N):
    for x in range(M):
        visited[y][x] = 1
        backtracking([(y, x)], 1, board[y][x])

print(ans)