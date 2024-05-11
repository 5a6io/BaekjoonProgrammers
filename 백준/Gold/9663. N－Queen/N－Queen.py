import sys
input = sys.stdin.readline

def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


def dfs(x):
    global answer
    if x == n:
        answer += 1
        return

    for i in range(n):
        if visited[i]:
            continue
        row[x] = i
        if adjacent(x):
            visited[i] = True
            dfs(x + 1)
            visited[i] = False


n = int(input())
row = [0] * n
visited = [False] * n
answer = 0

dfs(0)
print(answer)