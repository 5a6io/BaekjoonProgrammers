def solution(message, spoiler_ranges):
    answer = 0
    status = [0] * len(message)
    important = set()
    unimportant = set()
    
    for s, e in spoiler_ranges:
        for i in range(s, e+1):
            status[i] = 1
    
    words = []
    idx = 0
    for i, m in enumerate(message):
        if m == ' ':
            words.append((message[idx:i], idx, i-1))
            idx = i+1
    words.append((message[idx:], idx, len(message)-1))
    
    for w, s, e in words:
        for i in range(s, e+1):
            if status[i]:
                break
        else:
            unimportant.add(w)
            
    for start, end in spoiler_ranges:
        for w, s, e in words:
            if not (e < start or end < s):
                if w not in unimportant and w not in important:
                    important.add(w)
    
    answer = len(important)
    return answer