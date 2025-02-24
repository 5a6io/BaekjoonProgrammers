import sys
import heapq

input = sys.stdin.readline

N = int(input())
rooms = [list(map(int, input().split())) for _ in range(N)]
rooms.sort()

q = [rooms[0][1]]
for i in range(1, N):
    if q[0] <= rooms[i][0]:
        heapq.heappop(q)
    heapq.heappush(q, rooms[i][1])

print(len(q))