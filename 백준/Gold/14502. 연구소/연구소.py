import sys
import copy
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split()) # N = 세로, M = 가로
labs = [list(map(int, input().split())) for _ in range(N)]
# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    global ans
    virus = copy.deepcopy(labs) # 기존 배열의 변경이 복사본에 영향을 주지 않도록 하기 위해 깊은 복사를 함.

    q = deque()
    for y in range(N):
        for x in range(M):
            if virus[y][x] == 2:
                q.append((y, x))

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if virus[ny][nx] == 0:
                    virus[ny][nx] = 2
                    q.append((ny, nx))

    res = 0
    for i in range(N):
        res += virus[i].count(0)
    ans = max(res, ans)


def backtraking(w):
    if w == 3: # 벽을 세 개 세운 후 안전 지대 넓이 확인
        bfs()
        return

    for y in range(N):
        for x in range(M):
            if labs[y][x] == 0:
                labs[y][x] = 1
                backtraking(w+1)
                labs[y][x] = 0

ans = 0
backtraking(0)
print(ans)