for test_case in range(1, 11):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    dir = [[1, 0], [0, 1], [0, -1]]
    answer = 0

    for i in range(100):
        if ladder[0][i]:
            x, y = 0, i
            d = 0
            while x < 99:
                if d == 0:
                    if y > 0 and ladder[x][y - 1] == 1:
                        d = 2
                    elif y < 99 and ladder[x][y + 1] == 1:
                        d = 1
                else:
                    if ladder[x + 1][y] == 1:
                        d = 0

                x += dir[d][0]
                y += dir[d][1]

            if ladder[x][y] == 2:
                answer = i
                break

    print(f"#{t} {answer}")
