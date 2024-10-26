def solution(jobs):
    answer, time = 0, 0
    jobs.sort(key = lambda x : x[1])
    n = len(jobs)
    
    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= time:
                time += jobs[i][1]
                answer += time - jobs[i][0]
                jobs.pop(i)
                break
            if len(jobs) - 1 == i:
                time += 1
    
    return answer // n