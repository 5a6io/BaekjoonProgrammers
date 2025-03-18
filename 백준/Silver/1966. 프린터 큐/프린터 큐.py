import sys

input = sys.stdin.readline

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    D = list(zip(list(map(int, input().split())), range(N)))
    cnt = 1
    while D:
        mx = max(D)[0]
        d = D.pop(0)
        if d[0] < mx:
            D.append(d)
        elif d[0] == mx:
            if d[1] == M:
                print(cnt)
                break
            else:
                cnt += 1