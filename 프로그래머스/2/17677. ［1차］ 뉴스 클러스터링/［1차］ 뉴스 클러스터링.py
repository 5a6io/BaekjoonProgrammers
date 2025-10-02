from collections import Counter

def solution(str1, str2):
    _str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    _str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    if not _str1 and not _str2:
        return 65536
        
    c1, c2 = Counter(_str1), Counter(_str2)
    union = sum((c1|c2).values())
    inter = sum((c1&c2).values())
    
    return int(inter/union*65536)