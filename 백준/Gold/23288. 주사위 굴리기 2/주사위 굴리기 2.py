import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split()) # N 세로 크기, M 가로 크기, 이동하는 횟수 K
board = [list(map(int, input().split())) for _ in range(N)]
# 동 남 서 북
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 1 -> 윗면, 6 -> 아랫면
dice = [2, 1, 4, 3, 5, 6]
q = deque([(0, 0, 0)]) # y, x, d
k = 0
result = 0

def score(y, x):
    visited = [[False for _ in range(M)] for _ in range(N)]
    q = deque([(y, x)])
    count = 1
    visited[y][x] = True
    while  q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and board[ny][nx] == board[y][x]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    count += 1

    return count

def rotate_dice(d):
    if d == 0:
        dice[1], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[1], dice[3]
    elif d == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[5], dice[0], dice[1], dice[4]
    elif d == 2:
        dice[1], dice[2], dice[3], dice[5] = dice[3], dice[1], dice[5], dice[2]
    elif d == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[4], dice[5], dice[0]

while q and k < K:
    y, x, d = q.popleft()
    if y + dy[d] < 0 or y+dy[d] >= N or x + dx[d] < 0 or x + dx[d] >= M:
        d = (d + 2) % 4
    y += dy[d]
    x += dx[d]
    rotate_dice(d)
    if board[y][x] < dice[5]:
        d = (d+1) % 4
    elif board[y][x] > dice[5]:
        d = (d-1) % 4

    result += board[y][x] * score(y, x)
    q.append((y, x, d))

    k += 1

print(result)