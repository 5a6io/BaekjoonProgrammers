from collections import deque


def dfs(v):
    stack.append(v + 1)
    visited[v] = True

    for i in range(N):
        if graph[v][i] == 1 and not visited[i]:
            dfs(i)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    visit = [v+1]
    while queue:
        now = queue.popleft()

        for i in range(len(graph[now])):
            if graph[now][i] and not visited[i]:
                queue.append(i)
                visit.append(i+1)
                visited[i] = True

    print(*visit)


N, M, V = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(N)]

for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1 - 1][v2 - 1] = 1
    graph[v2 - 1][v1 - 1] = 1


visited = [False]*N
stack = list()
dfs(V - 1)
print(*stack)
visited = [False]*N
bfs(V - 1)