def solution(n, words):
    answer = [0, 0]

    said = set()

    prev = words[0][-1]
    said.add(words[0])
    for i in range(1, len(words)):
        if words[i][0] != prev or words[i] in said:
            answer[0] = i % n + 1
            answer[1] = i // n + 1
            break
        prev = words[i][-1]
        said.add(words[i])

    return answer