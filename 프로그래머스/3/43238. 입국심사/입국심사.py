def solution(n, times):
    answer = 0
    times.sort()
    s, e = times[0], n*times[0]
    while s <= e:
        m = (s + e) // 2
        p = 0
        for time in times:
            p += m // time
        
        if p >= n:
            answer = m
            e = m - 1
        else:
            s = m + 1
    
    return answer