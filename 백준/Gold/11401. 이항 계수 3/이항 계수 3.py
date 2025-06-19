import sys

input = sys.stdin.readline
MOD = 1000000007

def fact(N):
    if N <= 1:
        return 1

    res = 1
    for i in range(2, N+1):
        res *= i
        res %= MOD

    return res

def col(N, K):
    if K == 0 or N == K:
        return 1
    if K == 1:
        return N

    res = col(N, K//2)
    if K%2 == 0:
        return res * res % MOD
    else:
        return res * res * N % MOD

N, K = map(int, input().split())

num = fact(N)
den = fact(K) * fact(N - K)

print(num * col(den, MOD - 2) % MOD)