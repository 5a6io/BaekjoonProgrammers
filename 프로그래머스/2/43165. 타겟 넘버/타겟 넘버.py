def dfs(sum, numbers, i, target):
    if i == len(numbers):
        if sum == target:
            return 1
        else:
            return 0

    return dfs(sum + numbers[i], numbers, i+1, target)+ dfs(sum - numbers[i], numbers, i+1, target)

def solution(numbers, target):
    return dfs(0, numbers, 0, target)