def solution(clothes):
    answer = 1
    
    dic = dict()
    for _, kind in clothes:
        if kind not in dic:
            dic[kind] = 1
        else:
            dic[kind] += 1
    
    for k in dic.values():
        answer *= k + 1 # 각 의상의 수 + 안 입는 경우
    
    return answer - 1