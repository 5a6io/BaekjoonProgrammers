N, B = map(int, input().split())
s = []
while N > 0:
    N, m = divmod(N, B)
    s.append(m)

res = ""
dic = dict(zip(range(10, 36), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
while s:
    cur = s.pop()
    if cur >= 10:
        res += dic[cur]
    else:
        res += str(cur)

print(res)