import sys

input = sys.stdin.readline

N, B = map(int, input().split())
res = ''
dic = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while N > 0:
    N, m = divmod(N, B)
    res += dic[m]

print(res[::-1])