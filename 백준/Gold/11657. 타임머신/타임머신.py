import sys

input = sys.stdin.readline

N, M = map(int, input().split())
INF = 1e9
edges = [list(map(int, input().split())) for _ in range(M)]
dist = [0 if v == 0 else INF for v in range(N)]

def bellmanford(v):
    for v in range(N):
        for a, b, c in edges:
            if dist[a-1] != INF and dist[b-1] > dist[a-1] + c:
                dist[b-1] = dist[a-1] + c
                if v == N-1:
                    print(-1)
                    return
    for v in range(1, N):
        print(dist[v] if dist[v] != INF else -1)

bellmanford(0)