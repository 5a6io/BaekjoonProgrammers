import sys

input = sys.stdin.readline

N = int(input())
pos = [list(map(int, input().split())) for _ in range(N)]
pos.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(*pos[i], sep=' ')