for tc in range(10):
    l = int(input())
    bracket = list(input())

    st = []
    for b in bracket:
        if b == '(' or b == '[' or b == '<' or b == '{':
            st.append(b)
        else:
            if st:
                if b == ')' and st[-1] == '(':
                    st.pop()
                elif b == ']' and st[-1] == '[':
                    st.pop()
                elif b == '}' and st[-1] == '{':
                    st.pop()
                elif b == '>' and st[-1] == '<':
                    st.pop()
                else:
                    break

    if st:
        print(f"#{tc+1} 0")
    else:
        print(f"#{tc+1} 1")