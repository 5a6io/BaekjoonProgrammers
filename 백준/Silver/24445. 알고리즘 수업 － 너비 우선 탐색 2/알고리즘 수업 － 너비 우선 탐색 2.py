import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

for i in range(1, N+1):
    graph[i].sort(reverse=True)

def bfs():
    q = deque()
    q.append(R)
    visited[R] = 1
    cnt = 2
    while q:
        u = q.popleft()
        for v in graph[u]:
            if not visited[v]:
                q.append(v)
                visited[v] = cnt
                cnt += 1

bfs()
for i in range(1, N+1):
    if not visited[i]:
        print(0)
    else:
        print(visited[i])