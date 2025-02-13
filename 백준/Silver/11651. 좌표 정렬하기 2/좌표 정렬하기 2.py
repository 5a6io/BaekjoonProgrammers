import sys

input = sys.stdin.readline

N = int(input())
pos = [list(map(int, input().split())) for _ in range(N)]
pos.sort(key=lambda x: (x[1], x[0]))

for x, y in pos:
    print(x, y)