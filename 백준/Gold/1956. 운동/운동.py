import sys

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
board = [[INF if i != j else 0 for j in range(V)] for i in range(V)]

for _ in range(E):
    a, b, c = map(int, input().split())
    board[a-1][b-1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

res = INF
for v in range(V):
    for u in range(V):
        if u!= v:
            res = min(res, board[v][u] + board[u][v])
        
print(-1) if res >= INF else print(res)