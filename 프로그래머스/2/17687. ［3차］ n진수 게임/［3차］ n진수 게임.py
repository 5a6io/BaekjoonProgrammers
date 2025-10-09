def solution(n, t, m, p):
    answer = '0'
    dic = dict(zip(range(0, 16), '0123456789ABCDEF'))
    
    for i in range(1, t*m):
        num = ''
        while i:
            num += dic[i%n]
            i //= n
        answer += num[::-1]
    
    return answer[p-1:t*m:m]