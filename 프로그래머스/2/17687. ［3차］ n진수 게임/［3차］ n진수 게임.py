dic = dict(zip(range(0, 16), '0123456789ABCDEF'))

def trans(a, n):
    num = ''
    if a == 0:
        return '0'
    while a:
        num += dic[a%n]
        a //= n
        
    return num[::-1]

def solution(n, t, m, p):
    answer = ''
    
    for i in range(n**m+1):
        if len(answer) >= t*m+1:
            break
        answer += trans(i, n)
    
    return answer[p-1:t*m:m]