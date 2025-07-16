def solution(sizes):
    answer = max(max(s) for s in sizes) * max(min(s) for s in sizes)
    return answer