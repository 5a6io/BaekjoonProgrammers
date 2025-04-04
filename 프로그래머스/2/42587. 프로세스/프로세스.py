from collections import deque

def solution(priorities, location):
    answer = 1
    q = list(zip(priorities, range(len(priorities))))
    
    mx = max(q)[0]
    
    while q:
        p, i = q.pop(0)
        
        if p == mx:
            if i == location:
                break
            answer += 1
            mx = max(q)[0]
        else:
            q.append((p, i))
    
    return answer