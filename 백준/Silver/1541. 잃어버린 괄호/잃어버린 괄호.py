import sys
input = sys.stdin.readline
S = input().strip().split('-')
result = 0
for i in S[0].split('+'):
    result += int(i)
for i in S[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)