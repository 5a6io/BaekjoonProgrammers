import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
nodes = list(map(int, input().split()))
remove = int(input())
tree = defaultdict(list)
visited = [False] * N

def dfs(r):
    visited[r] = True
    for n in tree[r]:
        if not tree[n]:
            visited[n] = True
            tree.pop(n)
        else:
            dfs(n)
    tree.pop(r)

for v in range(N):
    if nodes[v] == -1:
        continue
    tree[nodes[v]].append(v)

dfs(remove)
res = 0

for n in range(N):
    if not visited[n]:
        if remove in tree[n] and len(tree[n])-1 == 0:
            res +=1
        if not tree[n]:
            res += 1

print(res)