import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
dic = defaultdict(int)

equation = input().rstrip()

for i in range(N):
    dic[chr(ord('A')+i)] = int(input())

st = []
for e in equation:
    if st:
        if e == '*':
            st.append(st.pop()*st.pop())
        elif e == '+':
            st.append(st.pop()+st.pop())
        elif e == '/':
            x1 = st.pop()
            x2 = st.pop()
            st.append(x2/x1)
        elif e == '-':
            x1 = st.pop()
            x2 = st.pop()
            st.append(x2-x1)
        else:
            st.append(dic[e])
    else:
        st.append(dic[e])

print(format(st[-1], '.2f'))