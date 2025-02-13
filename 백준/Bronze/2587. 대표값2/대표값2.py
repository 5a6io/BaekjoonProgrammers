import sys

input = sys.stdin.readline

a = [int(input()) for _ in range(5)]
a.sort()
print(sum(a)//5)
print(a[5//2])