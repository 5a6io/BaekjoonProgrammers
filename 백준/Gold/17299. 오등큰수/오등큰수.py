import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dic = defaultdict(int)
for a in A:
    dic[a] += 1

st = []
res = [-1] * N
for i in range(N-1):
    if dic[A[i]] < dic[A[i+1]]:
        res[i] = A[i+1]
        while st and dic[A[i+1]] > dic[st[-1][1]]:
            res[st.pop()[0]] = A[i+1]
    else:
        st.append((i, A[i]))

print(*res)