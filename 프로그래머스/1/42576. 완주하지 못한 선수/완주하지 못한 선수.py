def solution(participant, completion):    
    dic = {}
    for p in participant:
        if p not in dic:
            dic[p] = 1
        else:
            dic[p] += 1
    
    for c in completion:
        if dic[c] > 1:
            dic[c] -= 1
        else:
            dic.pop(c)
    
    return list(dic.keys())[0]