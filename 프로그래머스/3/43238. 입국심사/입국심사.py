def solution(n, times):
    answer = 0
    s, e = 1, n*max(times)
    while s <= e:
        m = (s + e) // 2
        p = 0
        for time in times:
            p += m//time
        if p >= n:
            answer = m
            e = m - 1
        else:
            s = m + 1
    
    return answer