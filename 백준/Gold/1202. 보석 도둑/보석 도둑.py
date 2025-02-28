import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, K = map(int, input().split())
jewelry = [list(map(int, input().split())) for _ in range(N)]
jewelry.sort()

bags = [int(input()) for _ in range(K)]
bags.sort()

temp = []
res = 0
for b in bags:
    while jewelry:
        if jewelry[0][0] <= b:
            heappush(temp, (-jewelry[0][1], jewelry[0][0]))
            heappop(jewelry)
        else:
            break

    if temp:
        res += -heappop(temp)[0]

print(res)