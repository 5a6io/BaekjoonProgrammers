def dfs(idx, c):
    global answer
    if c == int(n):
        answer = max(int(''.join(s)), answer)
        return
    for now in range(idx, len(s)):
        for mxi in range(now + 1, len(s)):
            if s[now] <= s[mxi]:
                s[now], s[mxi] = s[mxi], s[now]
                dfs(now, c+1)
                s[now], s[mxi] = s[mxi], s[now]

    if answer == 0 and c < int(n):
        if (int(n) - c) % 2 == 1:
            s[-1], s[-2] = s[-2], s[-1],
        dfs(idx, int(n))


T = int(input())

for test_case in range(1, T+1):
    s, n = input().split()
    s = list(s)
    answer = 0
    dfs(0, 0)

    print(f"#{test_case} {answer}")
