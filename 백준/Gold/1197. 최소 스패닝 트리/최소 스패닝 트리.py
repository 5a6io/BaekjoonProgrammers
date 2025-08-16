import sys

input = sys.stdin.readline
INF = 1e9

V, E = map(int, input().split())
graph = [[] for _ in range(V)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))

visited = [0] * V
dist = [INF] * V
dist[0] = 0

for _ in range(V):
    mn = INF
    b = -1
    for v in range(V):
        if not visited[v] and dist[v] < mn:
            mn = dist[v]
            b = v
    visited[b] = 1
    for u, c in graph[b]:
        if not visited[u]:
            dist[u] = min(dist[u], c)

print(sum(dist))