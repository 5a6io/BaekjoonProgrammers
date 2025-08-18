import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = 1e9

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
visited = [0] * n

for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a - 1].append((c, b - 1))
    edges[b - 1].append((c, a - 1))

ans = 0
q = [(0, 0)]

while q:
    c, v = heappop(q)

    if not visited[v]:
        visited[v] = 1
        ans += c

        for c, u in edges[v]:
            if not visited[u]:
                heappush(q, (c, u))

print(ans)