import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, list(input().strip()))) for _ in range(N)]
visited =[[False for _ in range(N)] for _ in range(N)]
res = []

def dfs(y, x):
    visited[y][x] = True
    cnt = graph[y][x]
    if 0 <= y + 1 < N:
        if not visited[y+1][x] and graph[y+1][x] == 1:
            cnt += dfs(y+1, x)
    if 0 <= x + 1 < N:
        if not visited[y][x+1] and graph[y][x+1] == 1:
            cnt += dfs(y, x+1)
    if 0 <= x - 1 < N:
        if not visited[y][x-1] and graph[y][x-1] == 1:
            cnt += dfs(y, x-1)
    if 0 <= y - 1 < N:
        if not visited[y-1][x] and graph[y-1][x] == 1:
            cnt += dfs(y-1, x)

    return cnt

for y in range(N):
    for x in range(N):
        if not visited[y][x] and graph[y][x] == 1:
            res.append(dfs(y, x))

res.sort()
print(len(res))
print(*res, sep='\n')