import sys

input = sys.stdin.readline
N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dice = [0, 0, 0, 0, 0, 0]
# 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def turn(o):
    if o == 1: # 동
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif o == 2: # 서
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif o == 3: # 북
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else: # 남
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]


for o in list(map(int, input().split())):
    nx, ny = x + dx[o - 1], y + dy[o - 1]
    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny
        turn(o)
        if board[x][y] == 0:
            board[x][y] = dice[5]
        else:
            dice[5] = board[x][y]
            board[x][y] = 0
        print(dice[0])