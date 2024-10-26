def solution(priorities, location):
    process=[(i, p) for i, p in enumerate(priorities)]
    answer = 0
    
    while True:
        cur = process.pop(0)
        if any(cur[1] < p[1] for p in process):
            process.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer