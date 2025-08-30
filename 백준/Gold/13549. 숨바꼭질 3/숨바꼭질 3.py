import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 1e9
N, K = map(int, input().split())
time = [INF] * 100001

def dijkstra():
    time[N] = 0
    move = []
    heappush(move, (0, N))

    while move:
        t, x = heappop(move)
        for nt, nx in [(t, x*2), (t+1, x+1), (t+1, x-1)]:
            if 0 <= nx <= 100000 and time[nx] > nt:
                time[nx] = nt
                heappush(move, (nt, nx))

dijkstra()
print(time[K])