def find_unimportant(message, spoiler_ranges):
    l = len(message)
    unimportant = set()
    status = [0] * l
    
    for s, e in spoiler_ranges:
        for i in range(s, e+1):
            if 0 <= i < l:
                status[i] = 1
    
    i = 0
    while i < l:
        if message[i].isspace():
            i += 1
            continue
        
        s = i
        while i < l and not message[i].isspace():
            i += 1
        
        e = i-1
        spoiler = False
        for j in range(s, e+1):
            if status[j]:
                spoiler = True
                break
        if not spoiler:
            unimportant.add("".join(message[s:e+1]))
    
    return unimportant
    
def find_important(s, e, message):
    l = len(message)
    start = s
    end = e
    if start < 0 or end >= l or start > end:
        return ""
        
    while start > 0 and not message[start - 1].isspace():
        start -= 1
        
    while end < l - 1 and not message[end + 1].isspace():
        end += 1
        
    return "".join(message[start:end+1])

def solution(message, spoiler_ranges):  
    unimportant = find_unimportant(message, spoiler_ranges)
    important = set()
                            
    for s, e in spoiler_ranges:
        word = find_important(s, e, message)
        for w in word.split():
            if w not in unimportant:
                important.add(w)
                
    return len(important)