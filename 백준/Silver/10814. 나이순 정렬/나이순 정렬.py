import sys

input = sys.stdin.readline

N = int(input())
M = []
for _ in range(N):
    age, name = input().strip().split()
    M.append([int(age), name]) # 나이를 정수형으로 바꾸지 않고 넣으면 정렬 부분에서 틀림

for m in sorted(M, key=lambda x: x[0]):
    print(m[0], m[1])