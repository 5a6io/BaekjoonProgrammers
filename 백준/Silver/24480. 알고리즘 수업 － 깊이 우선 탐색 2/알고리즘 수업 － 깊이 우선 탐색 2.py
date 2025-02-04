import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6) # recursion limit 늘리기

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

for i in range(1, N+1):
    graph[i].sort(reverse=True)

visited = [False] * (N+1)
cnt = 1
def dfs(u):
    global cnt
    visited[u] = cnt
    cnt += 1
    for v in graph[u]:
        if not visited[v]:
            dfs(v)

dfs(R)
for i in range(1, N+1):
    if not visited[i]:
        print(0)
    else:
        print(visited[i])