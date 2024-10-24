def solution(msg):
    dic = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1, 27)))

    answer = []

    j = 1
    w = msg[0]
    answer.append(dic[w])
    msg += " "
    for i in range(1, len(msg) - 1):
        tmp = w + msg[i]
        if tmp in dic:
            w = tmp
            if len(answer) != 0:
                answer.pop()
        else:
            dic[tmp] = 26 + j
            j += 1
            w = msg[i]
        answer.append(dic[w])
    
    return answer