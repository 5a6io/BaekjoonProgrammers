T = int(input())


def is_palindrome(s):
    n = len(s) - 1
    m = n // 2

    if s == s[::-1]:
        if s[:m] == s[:m][::-1] and s[m+1:] == s[m+1:][::-1]:
            return True
        else:
            return False
    else:
        return False


for test_case in range(1, T + 1):
    s = str(input())

    if is_palindrome(s):
        print("#" + str(test_case) + " YES")
    else:
        print("#" + str(test_case) + " NO")
