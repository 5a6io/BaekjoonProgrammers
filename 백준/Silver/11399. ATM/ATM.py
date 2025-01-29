import sys

input = sys.stdin.readline

N = int(input())
P = list(enumerate(list(map(int, input().split())), 1))
P.sort(key= lambda x: x[1])

res = [0] * (N+1)
for i in range(1, N+1):
    res[i] = res[i-1] + P[i-1][1]

print(sum(res))