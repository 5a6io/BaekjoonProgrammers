def solution(n, results):
    answer = 0
    INF = 1e9
    wins = [[0 if a == b else INF for b in range(n)] for a in range(n)] 
    loses = [[0 if a == b else INF for a in range(n)] for b in range(n)]
    
    for a, b in results:
        wins[a-1][b-1] = 1
        loses[b-1][a-1] = 1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if wins[i][j] > wins[i][k] + wins[k][j]:
                    wins[i][j] = wins[i][k] + wins[k][j]
                if loses[j][i] > loses[j][k] + loses[k][i]:
                    loses[j][i] = loses[j][k] + loses[k][i]
    
    for a in range(n):
        win = 0
        lose = 0
        for b in range(n):
            if a != b:
                if wins[a][b] != INF:
                    win += 1
                if loses[a][b] != INF:
                    lose += 1
        if win + lose == n-1:
            answer += 1
                
    return answer