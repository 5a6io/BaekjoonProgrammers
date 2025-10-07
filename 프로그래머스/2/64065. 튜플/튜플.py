def solution(s):
    answer = []
    for l in sorted(list(s.strip('{{').strip('}}').split('},{')), key=len):
        tmp = list(map(int, l.split(',')))
        
        for i in range(len(tmp)):
            if tmp[i] not in answer:
                answer.append(tmp[i])
    
    return answer