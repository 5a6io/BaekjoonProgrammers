import sys

input = sys.stdin.readline

N = int(input())
coun = [list(map(int, input().split())) for _ in range(N)]
dp=[0]*(N+1)
for i in range(N):
    t, p = coun[i]
    dp[i] = max(dp[i], dp[i - 1])
    if i+t <= N:
        dp[i+t] = max(dp[i+t], dp[i]+p)

print(max(dp))