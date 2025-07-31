import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
r, c, d = map(int, input().strip().split())
room = [list(map(int, input().strip().split())) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def checked(r, c):
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            return True
    return False

def cleaning(r, c, d):
    global room
    ans = 0

    while True:
        if room[r][c] == 0:
            ans += 1
            room[r][c] = 2

        if checked(r, c):
            for i in range(1, 5):
                dir = (d - i) % 4
                nr, nc = r + dr[dir], c + dc[dir]

                if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
                    d = dir
                    r, c = nr, nc
                    break

        else:
            nr, nc = r - dr[d], c - dc[d]
            if 0 > nr or nr >= N or 0 > nc or M <= nc or room[nr][nc] == 1:
                return ans
            r, c = nr, nc


print(cleaning(r, c, d))