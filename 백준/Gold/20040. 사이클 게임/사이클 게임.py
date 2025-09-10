import sys

input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(a, b):
    a, b = find(a), find(b)

    if find(a) > find(b):
        parent[a] = b
    else:
        parent[b] = a

for i in range(1, m+1):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)
    else:
        print(i)
        break
else:
    print(0)