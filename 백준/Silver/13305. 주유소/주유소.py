import sys

input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().split()))
gas = list(map(int, input().split()))

res = distance[0] * gas[0] # 다음 도시로 가기 위해서는 첫 도시에서 무조건 기름을 넣어야 함.
mn = gas[0]
for i in range(1, N - 1): # 마지막 주유소에서는 기름을 안 채움.
    mn = min(mn, gas[i])
    res += mn * distance[i]

print(res) # 2 * 5 + 2 * (3 + 1) = 18