def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse=True)

    if citations[0] == 0:
        return answer

    for h in range(len(citations)):
        if citations[h] > h:
            answer += 1

    return answer