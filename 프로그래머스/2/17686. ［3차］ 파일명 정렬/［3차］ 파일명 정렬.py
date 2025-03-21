def solution(files):
    answer = []

    for file in files:
        head, num, tail = '', '', ''
        for i in range(len(file)):
            if file[i].isdigit():
                num += file[i]
            elif not num:
                head += file[i]
            else:
                tail = file[i:]
                break
        answer.append((head, num, tail))
        
    answer.sort(key= lambda x: (x[0].upper(), int(x[1])))
        
    return [''.join(a) for a in answer]