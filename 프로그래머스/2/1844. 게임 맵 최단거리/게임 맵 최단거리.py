from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = n*m
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque([(0, 0)])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    visited[0][0] = 1
    while q:
        cy, cx = q.pop()
        
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if (ny, nx) == (n-1, m-1):
                    answer = min(answer, visited[cy][cx] + maps[ny][nx])
                if not visited[ny][nx] and maps[ny][nx]:
                    visited[ny][nx] = visited[cy][cx] + maps[ny][nx]
                    q.appendleft((ny, nx))
    
    if visited[n-1][m-1] == 0:
        answer = -1
                    
    return answer