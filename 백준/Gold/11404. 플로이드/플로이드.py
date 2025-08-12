import sys

input = sys.stdin.readline

# n = bus(vertex), m = busline(edge)
n = int(input())
m = int(input())
INF = 1e9
cities = [[0 if a == b else INF for b in range(n)] for a in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    cities[a-1][b-1] = min(cities[a-1][b-1], c)
    
for k in range(n):
    for a in range(n):
        for b in range(n):
            cities[a][b] = min(cities[a][b], cities[a][k] + cities[k][b])
                
for a in range(n):
    for b in range(n):
        print(0 if cities[a][b] == INF else cities[a][b], end=' ')
    print()