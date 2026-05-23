def solution(k, dungeons):
    def backtracking(d, k):
        nonlocal answer
        
        can = False
        
        for i in range(len(dungeons)):
            if not visited[i] and dungeons[i][0] <= k:
                can = True
                visited[i] = 1
                backtracking(d+1, k-dungeons[i][1])
                visited[i] = 0
        
        if not can:
            answer = max(d, answer)
            return 
                
    
    answer = -1
    visited = [0] * len(dungeons)
    backtracking(0, k)
    
    return answer