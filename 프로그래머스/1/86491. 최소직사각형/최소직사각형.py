def solution(sizes):
    for size in sizes:
        size.sort()
    sizes.sort(reverse=True)
    
    w = sizes[0][0]
    h = sizes[0][1]
    for i in range(len(sizes)):
        if h < sizes[i][1]:
            h = sizes[i][1]
    
    return w*h