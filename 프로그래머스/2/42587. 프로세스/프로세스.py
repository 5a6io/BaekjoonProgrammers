def solution(priorities, location):
    process = [(x, y) for x, y in zip(range(len(priorities)), priorities)]
    answer = 0
    
    while True:
        now = process.pop(0)
        if any(now[1] < p[1] for p in process):
            process.append(now)
        else:
            answer += 1
            if location == now[0]:
                return answer