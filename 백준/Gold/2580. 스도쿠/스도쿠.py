def row(r, num):
    for c in range(9):
        if sudoku[r][c] == num:
            return False

    return True


def col(c, num):
    for r in range(9):
        if sudoku[r][c] == num:
            return False

    return True


def square(r, c, num):
    row = r // 3 * 3
    col = c - c % 3

    for i in range(row, row+3):
        for j in range(col, col+3):
            if sudoku[i][j] == num:
                return False

    return True


def backtracking(idx):
    if len(blank) == idx:
        for i in range(9):
            print(*sudoku[i])
        exit(0)

    r = blank[idx][0]
    c = blank[idx][1]
    for n in range(1, 10):
        if row(r, n) and col(c, n) and square(r, c, n):
            sudoku[r][c] = n
            backtracking(idx+1)
            sudoku[r][c] = 0


sudoku = [list(map(int, input().split())) for _ in range(9)]
blank = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i, j])

backtracking(0)