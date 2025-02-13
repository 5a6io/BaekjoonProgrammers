import sys

input = sys.stdin.readline

a = list(input().strip())
a.sort(reverse=True)
print(''.join(a))