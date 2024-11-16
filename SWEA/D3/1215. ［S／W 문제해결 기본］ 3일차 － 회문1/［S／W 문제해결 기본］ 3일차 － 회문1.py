for tc in range(1, 11):
    l = int(input())
    board = [list(input()) for _ in range(8)]
    t_board = list(map(list, zip(*board)))

    res = 0
    for i in range(8):
        for j in range(8-l+1):
            s = board[i][j:j+l]
            if s == s[::-1]:
                res += 1
            t_s = t_board[i][j:j+l]
            if t_s == t_s[::-1]:
                res += 1

    print(f"#{tc} {res}")