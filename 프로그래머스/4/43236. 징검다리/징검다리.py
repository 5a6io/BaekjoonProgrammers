def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    s, e = 0, distance
    while s <= e:
        m = (s + e) // 2
        md = int(1e9) # 각 지점 사이의 최소 거리
        cr = 0 # 현재 돌
        cnt = 0 # 제거한 바위 개수
        for rock in rocks:
            diff = rock - cr
            if diff < m:
                cnt += 1
            else:
                cr = rock
                md = min(md, diff)
        if cnt > n:
            e = m - 1
        else:
            s = m + 1
            answer = m
        
    return answer