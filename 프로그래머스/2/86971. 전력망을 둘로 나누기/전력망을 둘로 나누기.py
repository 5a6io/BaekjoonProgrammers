from collections import deque

def bfs(cut, n, wires):
    tower = [[] for _ in range(n + 1)]
    visit = [False] * (n + 1)
    q = deque()
    
    for i in range(len(wires)):
        if i == cut:
            continue
        v1, v2 = wires[i]
        tower[v1].append(v2)
        tower[v2].append(v1)
    
    q.appendleft(1)
    visit[1] = True
    while q:
        cur = q.pop()
        for v in tower[cur]:
            if not visit[v]:
                visit[v] = True
                q.appendleft(v)
    
    net1 = 0
    net2 = 0
    
    for i in range(1, n + 1):
        if visit[i]:
            net1 += 1
        else:
            net2 += 1
    
    return abs(net1 - net2)

def solution(n, wires):
    answer = n + 1
    
    for i in range(len(wires)):
        answer = min(answer, bfs(i, n, wires))
        
    return answer    