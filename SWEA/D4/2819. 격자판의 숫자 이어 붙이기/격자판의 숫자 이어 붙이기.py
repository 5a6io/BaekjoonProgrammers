T = int(input())

dy=[1, -1, 0, 0]
dx=[0, 0, 1, -1]
def dfs(y, x, res):
    global nums
    if len(res) == 7:
        if res not in nums:
            nums.add(res)
        return

    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < 4 and 0 <= nx < 4:
            dfs(ny, nx, res + board[y][x])


for tc in range(1, T + 1):
    board = [input().split() for _ in range(4)]
    nums = set()

    for y in range(4):
        for x in range(4):
            dfs(y, x, "")

    print(f"#{tc} {len(nums)}")