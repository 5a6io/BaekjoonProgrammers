def solution(n, arr1, arr2):
    answer = []
    
    for a, b in zip(arr1, arr2):
        answer.append(format(a|b, f'0{n}b').replace("0", " ").replace("1", "#"))
    return answer