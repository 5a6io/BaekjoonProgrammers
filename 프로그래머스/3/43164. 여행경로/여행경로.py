from collections import defaultdict

def solution(tickets):
    answer = []
    airports = defaultdict(list)

    for f, t in tickets:
        airports[f].append(t)

    for airport in airports:
        airports[airport].sort(reverse=True)

    stack = ["ICN"]
    while stack:
        route = stack[-1]
        if not airports[route]:
            answer.append(stack.pop())
        else:
            next = airports[route].pop()
            stack.append(next)

    return answer[::-1]