import sys

input = sys.stdin.readline

N = int(input())
times = []
for _ in range(N):
    s, e = map(int, input().split())
    times.append((e, s))

times.sort()

end = -1
cnt = 0

for e, s in times:
    if s >= end:
        end = e
        cnt += 1

print(cnt)