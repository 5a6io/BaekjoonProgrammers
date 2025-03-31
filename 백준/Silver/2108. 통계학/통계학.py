import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
a = []
num = defaultdict(int)
sum = 0

for _ in range(N):
    x = int(input())
    a.append(x)
    num[x] += 1
    sum += x

a.sort()
# 산술평균
print(round(sum/N))
# 중앙값
print(a[N//2])
# 최빈값
fre = max(num.values())
st = []
for i in sorted(num.keys()):
    if num[i] == fre:
        st.append(i)
if len(st) > 1:
    print(st[1])
else:
    print(st[0])
# 범위
print(a[N-1] - a[0])