import sys

input = sys.stdin.readline

n = int(input())
lengths = list(map(int, input().split()))
prices = list(map(int, input().split()))
dp = [0] * (n - 1)
dp[0] = lengths[0] * prices[0]

minCost = prices[0]
for i in range(1, n - 1):
    if minCost > prices[i]:
        minCost = prices[i]
    dp[i] = dp[i - 1] + minCost * lengths[i]

print(dp[n - 2])