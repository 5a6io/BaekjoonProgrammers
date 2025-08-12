import sys

input = sys.stdin.readline

N = int(input())
dp = ["CY", "SK"]

print(dp[N%2]) 