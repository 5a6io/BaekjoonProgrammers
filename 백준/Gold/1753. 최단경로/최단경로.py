import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
adjlist = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    adjlist[u].append((v, w))

pq = []
heapq.heappush(pq, (0, K))
dist = [1e9] * (V+1)
dist[K] = 0

while pq:
    d, cur = heapq.heappop(pq)

    for v, w in adjlist[cur]:
        if dist[v] > dist[cur] + w:
            dist[v] = dist[cur] + w
            heapq.heappush(pq, (dist[v], v))

for i in range(1, V+1):
    if dist[i] == 1e9:
        print("INF")
    else:
        print(dist[i])