def solution(operations):
    answer = []
    
    q = []
    
    for o in operations:
        a, n = o.split(" ")
        if a == "I":
            q.append(int(n))
        else:
            if len(q) > 0:
                if n == "1":
                    q.remove(max(q))
                else:
                    q.remove(min(q))
    
    if len(q) == 0:
        answer = [0, 0]
    else:
        answer.append(max(q))
        answer.append(min(q))
    
    return answer