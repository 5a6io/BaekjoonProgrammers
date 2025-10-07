def solution(s):
    answer = []
    l = list(s.strip('{{').strip('}}').split('},{'))
    l.sort(key=len)
    for i in range(len(l)):
        c = list(map(int, l[i].split(',')))
        for j in range(len(c)):
            if c[j] not in answer:
                answer.append(c[j])
    
    return answer