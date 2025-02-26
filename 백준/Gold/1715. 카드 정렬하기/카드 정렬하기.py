import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
card = [int(input()) for _ in range(N)]
card.sort()

res = 0
while len(card) > 1:
    a, b = heappop(card), heappop(card)
    heappush(card, a + b)
    res += (a + b)

print(res)