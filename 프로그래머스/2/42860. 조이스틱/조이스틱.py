def solution(name):
    answer = 0
    cursor = len(name) - 1 # 좌우 최소 조작 횟수
    
    for i, s in enumerate(name):
        answer += min(ord(s) - ord('A'), ord('Z') - ord(s) + 1)
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        move = min(i, len(name) - next)
        cursor = min(cursor, i + len(name) - next + move)
            
    return answer + cursor