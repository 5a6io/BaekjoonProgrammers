def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    s, e = 0, distance
    while s <= e:
        m = (s + e) // 2
        cr = 0 # 현재 돌
        cnt = 0 # 제거한 바위 개수
        for rock in rocks:
            if rock - cr < m:
                cnt += 1
            else:
                cr = rock
        if cnt > n:
            e = m - 1
        else:
            s = m + 1
            answer = m
        
    return answer