t = int(input())

def dfs(s, c, d):
    global ms
    if c > l:
        return 
    ms = max(ms, s)
    if d == n:
        return

    dfs(s + scores[d], c + calories[d], d+1)
    dfs(s, c, d+1)


for i in range(1, t + 1):
    n, l = map(int, input().split())
    scores = [0] * n
    calories = [0] * n

    for j in range(n):
        scores[j], calories[j] = map(int, input().split())

    ms = 0
    dfs(0, 0, 0)


    print(f"#{i} {ms}")