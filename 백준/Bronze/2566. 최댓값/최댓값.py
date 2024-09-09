m = [list(map(int, input().split())) for _ in range(9)]

mx = -1
col, row = 0, 0
for i in range(9):
    if mx < max(m[i]):
        mx = max(m[i])
        col = i + 1
        row = m[i].index(mx) + 1

print(mx)
print(col, row, sep=" ")