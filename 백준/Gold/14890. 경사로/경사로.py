import sys

input = sys.stdin.readline

n, l = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(n)]
roads_tr = list(map(list, zip(*roads)))
answer = 0

def dfs(road):
    global answer
    visited = [False] * n #경사로를 이미 놓았는지 여부 체크
    for i in range(1, n):
        if abs(road[i] - road[i-1]) > 1:
            break
        elif abs(road[i] - road[i-1]) == 1:
            k = 0
            if road[i] > road[i-1]:
                while i-1-k > -1 and not visited[i-1-k] and road[i-1-k] == road[i]-1 and k != l:
                    visited[i-1-k] = True
                    k+=1
            elif road[i] < road[i-1]:
                while i+k < n and not visited[i+k] and road[i+k] == road[i-1]-1 and k != l:
                    visited[i+k] = True
                    k+=1
            if k < l:
                break
    else:
        answer += 1

for i in range(n):
    dfs(roads[i])
    dfs(roads_tr[i])

print(answer)