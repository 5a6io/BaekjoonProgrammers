n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
a = [[0 for _ in range(100)] for _ in range(100)]

for i in range(n):
    for x in range(p[i][0], p[i][0]+10):
        for y in range(p[i][1], p[i][1]+10):
            if a[x][y] == 0:
                a[x][y] = 1

s = 0
for i in range(100):
    for j in range(100):
        if a[i][j] == 1:
            s += 1

print(s)