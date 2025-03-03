import sys
from itertools import combinations

input = sys.stdin.readline

S = list(input().strip())
st = []
indices = []

res = set()
for i in range(len(S)):
    if S[i] == '(':
        st.append(i)
    elif S[i] == ')':
        indices.append((st.pop(), i))

for i in range(len(indices)):
    for comb in combinations(indices, i+1):
        temp = S[:]
        for c in comb:
            temp[c[0]] = temp[c[1]] = ""
        res.add("".join(temp))

for s in sorted(list(res)):
    print(s)