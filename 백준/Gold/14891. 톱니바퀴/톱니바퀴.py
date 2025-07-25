from collections import deque

wheels = [deque(list(map(int, input()))) for _ in range(4)]
K = int(input())

def left(c, r):
    global wheels
    if c < 0:
        return
    if wheels[c+1][6] != wheels[c][2]:
        left(c - 1, -r)
        wheels[c].rotate(r)


def right(c, r):
    global wheels
    if c > 3:
        return

    if wheels[c-1][2] != wheels[c][6]:
        right(c + 1, -r)
        wheels[c].rotate(r)


for _ in range(K):
    n, r = map(int, input().split())
    left(n - 2, -r)
    right(n, -r)
    wheels[n - 1].rotate(r)

ans = 0
for i in range(4):
    if wheels[i][0]:
        ans += 2 ** i

print(ans)