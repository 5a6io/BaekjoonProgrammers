def solution(clothes):
    answer = 1
    
    dic = dict()
    for cloth, kind in clothes:
        if kind not in dic:
            dic[kind] = 1
        else:
            dic[kind] += 1
    
    for k in dic.values():
        answer *= k + 1
    
    return answer - 1