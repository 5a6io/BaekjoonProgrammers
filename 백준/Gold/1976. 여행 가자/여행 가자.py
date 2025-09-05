import sys

input = sys.stdin.readline

N = int(input()) # 도시 수
M = int(input()) # 여행 계획에 속한 도시 수
parent = [i for i in range(N)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for i in range(N):
    status = list(map(int, input().split()))
    for j in range(N):
        if status[j]:
            union(i, j)

plan = list(map(int, input().split())) # 여행 계획

for i in range(M-1):
    if parent[plan[i]-1] != parent[plan[i+1]-1]:
        print("NO")
        break
else:
    print("YES")