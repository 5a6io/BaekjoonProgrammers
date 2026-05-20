def solution(distance, rocks, n):
    answer = 0
    
    s, e = 0, distance
    rocks.sort()
    rocks.append(distance)
    
    while s <= e:
        mid = (s+e)//2
        r, p_r = 0, 0
        for rock in rocks:
            if rock - p_r < mid:
                r += 1
            else:
                p_r = rock
        if r > n:
            e  = mid-1
        else:
            answer = mid
            s = mid + 1
    
    return answer