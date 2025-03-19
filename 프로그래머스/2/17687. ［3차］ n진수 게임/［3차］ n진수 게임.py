dic = list('0123456789ABCDEF')

def find_n(num, n):
    res = ""
    if num < n:
        return dic[num]
    while num >= n:
        res += dic[num%n]
        num //= n

    res += dic[num]
    return "".join(res[::-1])


def solution(n, t, m, p):
    answer = ""
    i = 0
    while len(answer) < t*m:
        answer += find_n(i, n)
        i += 1
    
    return answer[p-1::m][:t]