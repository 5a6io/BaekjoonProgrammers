T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    costs = list(map(int, input().split()))

    answer = 0

    m = max(costs)
    buy = 0
    cost = 0

    for i in range(n):
        if m > costs[i]:
            buy += 1
            cost += costs[i]
        elif m == costs[i]:
            answer += (m * buy - cost)
            if i + 1 < n:
                m = max(costs[i + 1:n])
            cost = 0
            buy = 0

    print(f"#{test_case} {answer}")