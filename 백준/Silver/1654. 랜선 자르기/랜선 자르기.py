import sys
input = sys.stdin.readline


K, N = map(int, input().split())
lan = []
for i in range(K):
    lan.append(int(input()))

s = 1
e = max(lan)

while s <= e:
    mid = (s+e) // 2
    l = 0
    for i in lan:
        l += i//mid
    if l >= N:
        s = mid + 1
    else:
        e = mid - 1

print(e)