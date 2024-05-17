import sys
input = sys.stdin.readline


N, M = map(int, input().split())
tree = list(map(int, input().split()))

s = 1
e = max(tree)

while s <= e:
    mid = (s + e) // 2
    t = 0

    for i in tree:
        if i > mid:
            t += i - mid
    if t < M:
        e = mid - 1
    else:
        s = mid + 1

print(e)