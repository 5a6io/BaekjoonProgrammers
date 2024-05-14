N = int(input())

house = [[0, 0, 0] for i in range(N)]
house[0] = list(map(int, input().split()))

for i in range(1, N):
    a, b, c = map(int, input().split())
    house[i][0] = min(house[i - 1][1], house[i - 1][2]) + a
    house[i][1] = min(house[i - 1][0], house[i - 1][2]) + b
    house[i][2] = min(house[i - 1][0], house[i - 1][1]) + c

print(min(house[N-1]))
