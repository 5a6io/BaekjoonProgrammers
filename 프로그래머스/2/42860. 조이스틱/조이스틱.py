def solution(name):
    answer = 0
    l =len(name)
    move = l - 1 # 처음부터 끝까지 움직이는 경우
    for i, n in enumerate(name):
        answer += min(ord(n) - ord('A'), (ord('Z') - ord(n)) + 1)
    
        next = i + 1
        while next < l and name[next] == 'A':
            next += 1
        move = min([move, 2*i + len(name) - next, i + 2*(l - next)])
                
    answer += move
        
    return answer