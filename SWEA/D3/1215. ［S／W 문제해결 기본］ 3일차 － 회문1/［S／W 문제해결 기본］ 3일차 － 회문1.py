def palindromic(y, x, s):
    if len(s) == l:
        if s == "".join(s[-1::-1]):
            return 1
        else:
            return 0

    return palindromic(y, x + 1, s + board[y][x])

def t_palindromic(y, x, s):
    if len(s) == l:
        if s == "".join(s[-1::-1]):
            return 1
        else:
            return 0

    return t_palindromic(y, x + 1, s + t_board[y][x])


for tc in range(1, 11):
    l = int(input())
    board = [list(input()) for _ in range(8)]
    t_board = list(map(list, zip(*board)))

    res = 0
    for i in range(8):
        for j in range(8-l + 1):
            res += palindromic(i, j, "")
            res += t_palindromic(i, j, "")

    print(f"#{tc} {res}")