import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    work = []

    while i  < len(jobs):
        # 현 시점에서 처리할 수 있는 작업들 큐에서 대기(요청 시간이 같으면 수행시간이 작은 것부터 실행해야 하므로 최소힙 사용)
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(work, (j[1], j[0]))
        if work:
            cur = heapq.heappop(work)
            start = now
            now += cur[0]
            answer += (now - cur[1])
            i += 1
        else:
            now += 1
    return answer // len(jobs)