import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
turns = deque([input().split() for _ in range(L)]) # X초가 끝난 뒤에 뱀이 C 방향으로 90도 회전.
# 방향 전환 D = 오른쪽, L = 왼쪽
rotate = {'D': 1, 'L': -1}
# 북, 동, 남, 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def OutOfRange(y, x):
    return False if 0 < y <= N and 0 < x <= N else True

def game(y, x, d):
    t = 0
    move = deque([(y, x)])
    while True:
        ny, nx = y + dy[d], x + dx[d]
        if OutOfRange(ny, nx) or (ny, nx) in move: # 범위를 벗어나면 멈춤.
            break

        if [ny, nx] not in apples: # 사과가 없다면 꼬리 제거
            move.popleft()
        else: # 사과가 있으면 사과 제거
            apples.remove([ny, nx])
            
        y, x = ny, nx
        move.append((ny, nx))
        t += 1

        if turns and t == int(turns[0][0]):
            turn = turns.popleft()[1]
            d = (d + rotate[turn]) % 4 # 왼쪽 또는 오른쪽으로 90도 회전.

    return t+1

print(game(1, 1, 1)) # 오른쪽으로 향한다고 하였으므로 방향을 1로 함.