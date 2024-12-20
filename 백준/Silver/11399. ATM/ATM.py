import sys

input = sys.stdin.readline

n = int(input())
p = list(zip(range(1, n+1), list(map(int, input().split()))))
p.sort(key= lambda x: x[1])

answer = [p[0][1]]
for i in range(1, n):
    answer.append(answer[i-1] + p[i][1])

print(sum(answer))