dic = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10: "A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}

def find_n(num, n):
    res = ""
    if num < n:
        return dic[num]
    while num >= n:
        res += dic[num%n]
        num //= n

    res += dic[num]
    return "".join(reversed(res))


def solution(n, t, m, p):
    answer = ""
    temp = ""
    for i in range(t*m):
        if len(temp) > t*m:
            break
        temp += find_n(i, n)
    
    for i in range(t):
        if len(answer) > t:
            break
        answer += temp[p-1+i*m]
        
    return answer