import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
balloons = deque(enumerate(map(int, input().split())))
ans = []

while balloons:
    i, num = balloons.popleft()
    ans.append(i+1)
    if num > 0:
        balloons.rotate(-(num-1))
    else:
        balloons.rotate(-num)

print(*ans)