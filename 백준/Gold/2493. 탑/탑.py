import sys

input = sys.stdin.readline

N = int(input())
top = list(map(int, input().split()))
res = [0] * N
temp = []
for i in range(N):
    while temp:
        if temp[-1][1] > top[i]:
            res[i] = temp[-1][0]
            break
        else:
            temp.pop()

    temp.append((i+1, top[i]))

print(*res)