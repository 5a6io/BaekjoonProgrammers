import sys

input = sys.stdin.readline

N = int(input())
M = []
for _ in range(N):
    age, name = input().strip().split()
    M.append([int(age), name])

for m in sorted(M, key=lambda x: x[0]):
    print(m[0], m[1])