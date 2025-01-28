def solution(n, lost, reserve):
    answer = 0
    cnt = [0] * (n + 1)
    for i in range(1, n + 1):
        if i in lost:
            cnt[i] -= 1
        if i in reserve:
            cnt[i] += 1
        
    for i in range(1, n + 1):
        if cnt[i] == 1 and i - 1 != 0 and cnt[i - 1] < 0:
            cnt[i] = cnt[i-1] = 0
        if cnt[i] == 1 and i + 1 != n + 1 and cnt[i + 1] < 0:
            cnt[i] = cnt[i+1] = 0
            
    for i in range(1, n + 1):
        if cnt[i] > -1:
            answer += 1
    
    return answer