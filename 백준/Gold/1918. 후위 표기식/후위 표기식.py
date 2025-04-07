import sys

input = sys.stdin.readline

equation = input().rstrip()

res = []
st = []

for e in equation:
    if e == '(':
        st.append(e)
    elif e == ')':
        while st and st[-1] !=  '(':
            res.append(st.pop())
        st.pop()
    elif e == '*' or e == '/':
        while st and (st[-1] == '*' or st[-1] == '/'):
            res.append(st.pop())
        st.append(e)
    elif e == '+' or e == '-':
        while st and st[-1] != '(':
            res.append(st.pop())
        st.append(e)
    else:
        res.append(e)
while st:
    res.append(st.pop())

print("".join(res))