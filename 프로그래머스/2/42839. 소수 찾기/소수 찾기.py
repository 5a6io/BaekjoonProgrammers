from itertools import permutations

def solution(numbers):
    nums = set()
    for i in range(len(numbers)):
        nums |= set(map(int, map("".join, permutations(list(numbers), i + 1))))
    nums -= set(range(0, 2))
    for i in range(2, int(max(nums) ** 0.5) + 1):
        nums -= set(range(i * 2, max(nums)+ 1, i))

    return len(nums)