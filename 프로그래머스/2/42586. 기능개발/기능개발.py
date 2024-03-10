def solution(progresses, speeds):
    answer = []
    remain = []
    task = 1

    for i in range(len(speeds)):
        if (100-progresses[i])%speeds[i] != 0:
            remain.append(int((100-progresses[i])/speeds[i]) + 1)
        else:
            remain.append(int((100-progresses[i])/speeds[i]))

    m = remain[0]
    for i in range(1, len(remain)):
        if remain[i] <= m:
            task+=1
        else:
            answer.append(task)
            task = 1
            m = remain[i]

    answer.append(task)

    return answer