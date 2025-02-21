def solution(n, k):
    num = ""
    while n:
        num = str(n%k) + num
        n //= k
    
    num = num.split("0")
    
    answer = len(num)
    for x in num:
        if x == '' or int(x) == 0 or int(x) == 1:
            answer -= 1
            continue
        
        for i in range(2, int(int(x)**0.5)+1):
            if int(x)%i == 0:
                answer -= 1
                break
    
    return answer