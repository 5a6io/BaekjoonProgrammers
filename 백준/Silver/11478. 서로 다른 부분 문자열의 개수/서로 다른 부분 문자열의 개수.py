import sys

input = sys.stdin.readline

s = list(input().strip())
ans = set(s)

for i in range(len(s)):
    tmp = s[i]
    for j in range(i + 1, len(s)):
        tmp += s[j]
        ans.add(tmp)

print(len(ans))