def solution(n, computers):
    answer = 0
    visited = [False] * (n)

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            stack = [i]

            while len(stack) > 0:
                cur = stack.pop()
                visited[cur] = True

                for j in range(n):
                    if not visited[j] and computers[cur][j] == 1:
                        visited[j] = True
                        stack.append(j)

            answer += 1

    return answer