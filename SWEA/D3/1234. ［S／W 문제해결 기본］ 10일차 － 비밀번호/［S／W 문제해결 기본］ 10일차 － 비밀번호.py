for test_case in range(1, 11):
    N, P = input().split()
    pwd = list(P)

    stack = []
    for i in pwd:
        if len(stack) != 0 and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    print(f"#{test_case} ", *stack, sep='')
