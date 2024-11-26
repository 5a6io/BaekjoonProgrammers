def solution(N, number):
    if N == number:
        return 1
    
    dp = [set() for _ in range(9)]
    dp[1].add(N)
    x = N
    for i in range(2, 9):
        dp.append(set())
        x = 10 * x + N
        dp[i].add(x)
        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        
        if number in dp[i]:
            return i
        
    return -1