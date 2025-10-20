from collections import deque

def solution(n, edge):
    answer = 0
    dist = [1e9] * n
    dist[0] = 0
    edges = [[] for _ in range(n)]
    for v, u in edge:
        edges[v-1].append(u-1)
        edges[u-1].append(v-1)
        
    move = deque([(0, 0)]) # 거리, 정점
    while move:
        d, v = move.popleft()
        
        for u in edges[v]:
            if dist[u] > dist[v]+1:
                dist[u] = dist[v]+1
                move.append((dist[u], u))
                
    answer = dist.count(max(dist))
    
    return answer