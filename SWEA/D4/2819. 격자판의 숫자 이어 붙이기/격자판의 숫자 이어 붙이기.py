T = int(input())

def dfs(y, x, res):
    global nums
    if len(res) == 7:
        if res not in nums:
            nums.add(res)
        return

    if 0 <= y < 4 and 0 <= x < 4:
        dfs(y + 1, x, res + board[y][x])
        dfs(y - 1, x, res + board[y][x])
        dfs(y, x + 1, res + board[y][x])
        dfs(y, x - 1, res + board[y][x])


for tc in range(1, T + 1):
    board = [input().split() for _ in range(4)]
    nums = set()

    for y in range(4):
        for x in range(4):
            dfs(y, x, "")

    print(f"#{tc} {len(nums)}")