import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

dp = [0 for _ in range(n+1)]
R = [0 for _ in range(m)]
for i in range(1, n+1):
    dp[i] = array[i - 1] + dp[i - 1]
    R[dp[i] % m] += 1

answer = R[0]
for i in range(m):
    answer += R[i] * (R[i] - 1) // 2

print(answer)