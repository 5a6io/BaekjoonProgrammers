def solution(s):
    answer = []
    dic = dict(zip(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],"0123456789"))
    
    num = ''
    for c in s:
        if str.isdigit(c):
            answer.append(c)
        else:
            num += c
            if num in dic:
                answer.append(dic[num])
                num = ''
    
    return int(''.join(answer))