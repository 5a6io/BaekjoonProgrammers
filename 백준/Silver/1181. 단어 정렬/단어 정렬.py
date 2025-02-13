import sys

input = sys.stdin.readline

N = int(input())
S = list(set([input().strip() for _ in range(N)]))
S.sort(key=lambda x: (len(x), x))

for s in S:
    print(s)