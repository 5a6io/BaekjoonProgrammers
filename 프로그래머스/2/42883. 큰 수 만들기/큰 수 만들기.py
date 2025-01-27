def solution(number, k):
    answer = ''
    num = []
    for n in number:
        while len(num) > 0 and num[-1] < n and k > 0:
            num.pop()
            k -= 1
        num.append(n)
    
    return answer.join(num[:len(number)-k])