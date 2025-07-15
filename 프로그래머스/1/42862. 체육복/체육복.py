from collections import deque

def solution(n, lost, reserve):
    ls = set(lost) - set(reserve)
    rs = set(reserve) - set(lost)
    
    for r in rs:
        if r-1 in ls:
            ls.remove(r-1)
        elif r+1 in ls:
            ls.remove(r+1)
    
    return n - len(ls)