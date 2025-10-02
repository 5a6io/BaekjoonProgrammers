def solution(str1, str2):
    _str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    _str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if len(_str1) == 0 and len(_str2) == 0:
        return 65536
    union = len(_str1) + len(_str2)
    inter = []
    if len(_str1) > len(_str2):
        _str = _str2.copy()
        for s in _str1:
            if s in _str:
                _str.remove(s)
                inter.append(s)
    else:
        _str = _str1.copy()
        for s in _str2:
            if s in _str:
                _str.remove(s)
                inter.append(s)
    answer = int(len(inter)/(union-len(inter))*65536)
    return answer