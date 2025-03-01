import sys

input = sys.stdin.readline

N = int(input())
res = [0] * N
top = list(map(int, input().split()))
temp = []
for i in range(N):
    while temp and temp[-1][1] <= top[i]:
        temp.pop()
    if temp:
        res[i] = temp[-1][0]
    temp.append((i+1, top[i],))

print(*res)