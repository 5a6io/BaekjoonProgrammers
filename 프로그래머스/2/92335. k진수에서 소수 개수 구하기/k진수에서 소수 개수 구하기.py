def solution(n, k):
    answer = 0
    num = ''
    while n:
        num += str(n%k)
        n //= k
    num = num[::-1].split('0')
    
    for i in num:
        if len(i) == 0 or i == '1':
            continue
        # 에라토스테네스의 체 알고리즘
        for j in range(2, int(int(i)**(1/2))+1):
            if int(i)%j == 0:
                break
        else:
            answer += 1
    
    return answer