T = int(input())


def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or x - i == abs(row[x] - row[i]):
            return False
    return True


def dfs(x):
    global answer

    if x == n:
        answer += 1
    else:
        for i in range(n):
            row[x] = i # x행 i열에 퀸을 놓음.
            if adjacent(x): # x행의 상하좌우 대각선 확인
                dfs(x + 1)


for test_case in range(1, T + 1):
    n = int(input())
    answer = 0
    row = [0] * n

    dfs(0)

    print(f"#{test_case} {answer}")
