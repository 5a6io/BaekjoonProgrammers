import math

def solution(n, stations, w):
    answer = 0
    cover = w * 2 + 1
    
    start = 1
    for s in stations:
        uncovered = (s - w) - start
        
        if uncovered > 0:
            answer += math.ceil(uncovered / cover)
            
        start = s + w + 1
        
    if start <= n:
        uncovered = n - start + 1
        answer += math.ceil(uncovered / cover)

    return answer