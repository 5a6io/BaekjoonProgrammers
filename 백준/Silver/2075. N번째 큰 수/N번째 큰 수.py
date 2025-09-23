import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N  = int(input())
heap = []
for _ in range(N):
    for n in list(map(int, input().split())):
        if len(heap) < N:
            heappush(heap, n)

        if heap[0] < n:
            heappop(heap)
            heappush(heap, n)

print(heap[0])