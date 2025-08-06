import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split()) # N = 세로, M = 가로
labs = [list(map(int, input().split())) for _ in range(N)]

def bfs(walls):
    # 선택한 위치에 벽 세우기
    for y, x in walls:
        labs[y][x] = 1

    q = deque(virus)
    res = CNT - 3  # 벽 세운 개수를 빼고 남은 빈 칸
    visit = [[1 if (y, x) in virus else 0 for x in range(M)] for y in range(N)]

    while q:
        y, x = q.popleft()

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and visit[ny][nx] == 0 and labs[ny][nx] == 0:
                q.append((ny, nx))
                visit[ny][nx] = 1
                res -= 1

    for y, x in walls:
        labs[y][x] = 0

    return res


ans = 0
empty = []
virus = []

# 비어있는 곳과 바이러스가 있는 곳 탐색
for y in range(N):
    for x in range(M):
        if labs[y][x] == 0:
            empty.append((y, x))
        elif labs[y][x] == 2:
            virus.append((y, x))

# 비어있는 곳 중 한 곳을 벽을 세울 세 곳 선택
CNT = len(empty)
for i in range(CNT-2):
    for j in range(i+1, CNT-1):
        for k in range(j+1, CNT):
            ans = max(bfs([empty[i], empty[j], empty[k]]), ans)

print(ans)