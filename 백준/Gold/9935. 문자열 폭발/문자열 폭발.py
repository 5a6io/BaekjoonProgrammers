import sys

input = sys.stdin.readline

s = list(input().strip())
bomb = list(input().strip())

st = []
for i in range(len(s)):
    st.append(s[i])
    if len(st) >= len(bomb) - 1 and st[-len(bomb):] == bomb:
        for _ in range(len(bomb)):
            st.pop()

if len(st) != 0:
    print("".join(st))
else:
    print("FRULA")