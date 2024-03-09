def solution(clothes):
    answer = 1
    type = {}

    for i in clothes:
        type[i[1]] = type.get(i[1], 0)+1

    for i in type.values():
        answer *= (i+1)

    return answer - 1