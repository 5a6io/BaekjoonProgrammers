from collections import deque

def solution(n, edge):
    answer = 0
    dist = [1e9] * n
    dist[0] = 0
    edges = [[] for _ in range(n)]
    for v, u in edge:
        edges[v-1].append((1, u-1))
        edges[u-1].append((1, v-1))
        
    move = deque([(0, 0)]) # 거리, 정점
    while move:
        _, v = move.popleft()
        
        for d, u in edges[v]:
            if dist[u] > dist[v]+d:
                dist[u] = dist[v]+d
                move.append((dist[u], u))
                
    answer = dist.count(max(dist))
    
    return answer