def solution(sizes):
    answer = 0
    for size in sizes:
        size.sort(reverse=True)
    
    sizes.sort(key=lambda x: -x[0])
    
    w = sizes[0][0]
    for _, h in sizes:
        answer = max(answer, w*h)
               
    return answer