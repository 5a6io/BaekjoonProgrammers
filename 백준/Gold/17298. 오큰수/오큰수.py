import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
st = []
res = [-1] * n
for i in range(n-1):
    if A[i] < A[i+1]:
        res[i] = A[i+1]
        while st and st[-1][1] < A[i+1]:
            res[st.pop()[0]] = A[i+1]
    else:
        st.append((i, A[i]))

print(*res)