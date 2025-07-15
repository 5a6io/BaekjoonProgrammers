def solution(n, lost, reserve):
    rs = list(set(reserve)-set(lost))
    ls = list(set(lost)-set(reserve))
    
    for r in rs:
        p, b = r-1, r+1
        if p in ls:
            ls.remove(p)
        elif b in ls:
            ls.remove(b)
            
    return n-len(ls)