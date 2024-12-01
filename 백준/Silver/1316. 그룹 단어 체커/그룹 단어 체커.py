import sys

input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
cnt = n
for _ in range(n):
    s = list(input().strip())
    for i in range(len(s)):
        if s.index(s[i]) < i - 1:
            if s[i] == s[i-1]:
                continue
            else:
                cnt -= 1
                break

print(str(cnt))