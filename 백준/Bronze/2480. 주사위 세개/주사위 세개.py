cnt = [0 for _ in range(7)]
mx = 0
dice = list(map(int, input().split()))

for i in dice:
    cnt[i] += 1
    if i > mx:
        mx = i

m = max(cnt)
if m != 1:
    i = cnt.index(m)
    if m == 3:
        print(10000+i*1000)
    elif m == 2:
        print(1000+i*100)
else:
    print(mx * 100)