import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
v = int(input())

cnt = 0
for x in arr:
    if x == v:
        cnt += 1
        
print(cnt)