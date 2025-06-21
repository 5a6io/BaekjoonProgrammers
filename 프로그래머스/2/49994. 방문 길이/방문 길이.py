def solution(dirs):
    dy = {'U':-1,'D':1,'R':0,'L':0}
    dx = {'U':0,'D':0,'R':1,'L':-1}
    visited = set()
    cx, cy = 0, 0
    
    for d in dirs:
        if -5 <= cx + dx[d] <= 5 and -5 <= cy + dy[d] <= 5:
            visited.add(((cx, cy), (cx + dx[d], cy + dy[d])))
            visited.add(((cx + dx[d], cy + dy[d]), (cx, cy)))
            cx, cy = cx + dx[d], cy + dy[d]
    
    return len(visited)//2