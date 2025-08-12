import sys

input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
blue, white = 0, 0

def divide_and_conquer(y, x, n):
    global blue, white
    color = paper[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if color != paper[i][j]:
                divide_and_conquer(y, x, n//2)
                divide_and_conquer(y + n//2, x, n//2)
                divide_and_conquer(y, x + n//2, n//2)
                divide_and_conquer(y + n//2, x + n//2, n//2)
                return

    if color == 1:
        blue += 1
    else:
        white += 1

divide_and_conquer(0, 0, N)
print(white, blue, sep='\n')