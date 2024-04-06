from collections import deque

n = int(input())  # 노드의 개수

graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
answer = [0] * (n + 1)

for i in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

queue = deque([1])
visited[1] = True

while queue:
    x = queue.popleft()
    for i in graph[x]:
        if not visited[i]:
            answer[i] = x
            visited[i] = True
            queue.append(i)

for i in range(2, n + 1):
    print(answer[i])