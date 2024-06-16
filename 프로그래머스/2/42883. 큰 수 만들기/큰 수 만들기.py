def solution(number, k):
    num = list(number)
    stack = []
    
    l = len(num) - k

    for i in range(len(num)):
        while k > 0 and stack and stack[-1] < num[i]:
            stack.pop()
            k -= 1
            
        if k == 0:
            stack += num[i:]
            break

        stack.append(num[i])

    if len(stack) > l:
        stack = stack[:l]

    answer = ''.join(stack)
    
    return answer