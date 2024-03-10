import heapq

def solution(scoville, K):
    s = []
    for i in scoville:
        heapq.heappush(s, i)

    answer = 0
    while s[0] < K or len(s) < 1:
        if len(s) < 2 and s[0] < K:
            return -1
        first = heapq.heappop(s)
        second = heapq.heappop(s)

        new = first + (second * 2)
        heapq.heappush(s, new)
        answer += 1

    return answer