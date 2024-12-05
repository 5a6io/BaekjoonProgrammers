import sys

input = sys.stdin.readline
ts = int(input())

res = 0
for _ in range(ts):
    n, m = map(int, input().split())
    dp = [0] * (m+1)
    dp[0] = 1
    dp[1] = m

    for i in range(2, n+1):
        dp[i] = dp[i - 1]*(m-i+1)//i

    print(dp[n])