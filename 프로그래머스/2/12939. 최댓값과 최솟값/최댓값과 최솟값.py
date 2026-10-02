def solution(s):
    answer = list(map(int , s.split(' ')))
    answer = str(min(answer)) + " " + str(max(answer))
    return answer