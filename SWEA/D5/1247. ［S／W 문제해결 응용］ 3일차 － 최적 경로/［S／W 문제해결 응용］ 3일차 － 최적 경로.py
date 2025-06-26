def backtracking(visited, pre, cnt, dist):
    global res

    if cnt == N:
        r = abs(home[0]-clients[pre][0]) + abs(home[1]-clients[pre][1])
        res = min(res, dist+r)
        return

    for i in range(N):
        if not visited[i]:
            if cnt == 0:
                r = abs(company[0]-clients[i][0]) + abs(company[1]-clients[i][1])
                visited[i] = True
                backtracking(visited, i, cnt+1, dist+r)
                visited[i] = False
            else:
                visited[i] = True
                r = abs(clients[pre][0]-clients[i][0]) + abs(clients[pre][1]-clients[i][1])
                backtracking(visited, i, cnt+1, dist+r)
                visited[i] = False


test_case = int(input())
for tc in range(1, test_case+1):
    res = 1e9
    N = int(input()) # 고객 수
    visited = [False] * N

    # 회사, 집, 고객
    coords = list(map(int, input().split()))

    company = coords[:2]
    home = coords[2:4]
    clients = []
    for i in range(4, len(coords), 2):
        clients.append((coords[i], coords[i + 1]))

    backtracking(visited, -1, 0, 0)

    print(f"#{tc} {res}")