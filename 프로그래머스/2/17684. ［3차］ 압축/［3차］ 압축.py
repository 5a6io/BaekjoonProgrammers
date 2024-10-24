def solution(msg):
    dic = {"A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5, "F": 6, "G" : 7, "H" : 8, "I" : 9,
    "J" : 10, "K" : 11, "L": 12, "M": 13, "N" : 14, "O" : 15, "P" : 16, "Q" : 17, "R" : 18,
    "S" : 19, "T" : 20, "U" : 21, "V" : 22, "W" : 23, "X" : 24, "Y" : 25, "Z" : 26}

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