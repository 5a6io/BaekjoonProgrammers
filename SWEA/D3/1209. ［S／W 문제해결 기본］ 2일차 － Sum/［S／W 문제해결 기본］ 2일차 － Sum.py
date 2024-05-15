for test_case in range(1, 11):
    n = int(input())
    maze = [list(map(int, input().split())) for i in range(100)]
    t_maze = list(map(list, zip(*maze)))
    answer, answer1, answer2 = 0, 0, 0

    for i in range(100):
        answer = max(answer, max(sum(maze[i]), sum(t_maze[i])))
        answer1 += maze[i][i]
        answer2 += maze[i][99-i]

    answer = max(answer, max(answer1, answer2))

    print(f"#{test_case} {answer}")