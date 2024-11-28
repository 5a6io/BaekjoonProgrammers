import sys

input = sys.stdin.readline
n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times.sort(key= lambda x : (x[1], x[0]))

result = 0
time = -1
for s, e in times:
    if s >= time:
        time = e
        result += 1

print(result)