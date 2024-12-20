import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.sort()

answer = [p[0]]
for i in range(1, n):
    answer.append(answer[i-1] + p[i])

print(sum(answer))