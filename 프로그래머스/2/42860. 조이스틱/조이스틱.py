def solution(name):
    dic = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
    answer = 0
    cursor = len(name) - 1  # 오른쪽 왼쪽 최대 움직임
    
    for left in range(len(name)):
        sub_a = (dic[name[left]] - dic['A']) % 26
        sub_b = (dic['A'] - dic[name[left]]) % 26
        answer += min(sub_b, sub_a)
        
        idx = left + 1
        while idx < len(name) and name[idx] == 'A': idx += 1
        right = len(name) - idx
        move = min(left, len(name) - right)
        cursor = min(cursor, left + right + min(left, right))        
    
    return answer + cursor