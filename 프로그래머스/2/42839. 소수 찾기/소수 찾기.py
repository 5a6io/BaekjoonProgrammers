nums = set()

def isprime(num):
    if num == 0 or num == 1:
        return False
    i = 2
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def backtracking(length, numbers, visit, num):
    if len(num) == length:
        if isprime(int(num)):
            nums.add(int(num))
        return

    for i in range(len(numbers)):
        if not visit[i]:
            visit[i] = True
            backtracking(length, numbers, visit, num + numbers[i])
            visit[i] = False


def solution(numbers):
    visit = [False] * len(numbers)

    for i in range(1, len(numbers) + 1):
        for j in range(len(numbers)):
            if not visit[j]:
                visit[j] = True
                backtracking(i, numbers, visit, numbers[j])
                visit[j] = False

    return len(nums)