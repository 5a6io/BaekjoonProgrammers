N = int(input())

A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

mx = -1e9
mn = 1e9


def dfs(n, result):
    global add, sub, mul, div, mx, mn

    if n == N:
        mx = max(mx, result)
        mn = min(mn, result)
        return

    if add != 0:
        add -= 1
        dfs(n + 1, result + A[n])
        add += 1

    if sub != 0:
        sub -= 1
        dfs(n + 1, result - A[n])
        sub += 1

    if mul != 0:
        mul -= 1
        dfs(n + 1, result * A[n])
        mul += 1

    if div != 0:
        div -= 1
        dfs(n + 1, int(result / A[n]))
        div += 1


dfs(1, A[0])
print(int(mx), int(mn), sep='\n')