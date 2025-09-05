import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 1e9

N, E = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a-1].append((b-1, c))
    edges[b-1].append((a-1, c))
v1, v2 = map(int, input().split())

def dijkstra(start, end):
    dist = [INF] * N
    move = [(0, start)]
    dist[start] = 0
    
    while move:
        d, v = heappop(move)
        for u, c in edges[v]:
            if dist[u] > d + c:
                dist[u] = d + c
                heappush(move, (d + c, u))
    
    return dist[end]

# 1 -> v1 -> v2 -> N
c1 = dijkstra(0, v1-1) + dijkstra(v1-1, v2-1) + dijkstra(v2-1, N-1)

# 1 -> v2 -> v1 -> N
c2 = dijkstra(0, v2-1) + dijkstra(v2-1, v1-1) + dijkstra(v1-1, N-1)

print(-1) if c1 >= INF and c2 >= INF else print(min(c1, c2))