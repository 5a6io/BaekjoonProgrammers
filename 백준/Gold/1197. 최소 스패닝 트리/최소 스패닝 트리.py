import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
parent = list(range(V))
edges.sort(key= lambda x: x[2])
cost = 0

def find(x): # 특정 원소가 어느 그룹에 속하는지 찾기.
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b): # 두 그룹을 하나로 합치기.
    a, b = find(a), find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for a, b, c in edges:
    if find(a - 1) != find(b - 1):
        union(a - 1, b - 1)
        cost += c

print(cost)