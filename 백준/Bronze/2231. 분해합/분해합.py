n = int(input())

for i in range(1, n):
    res = sum(int(x) for x in str(i))
    res += i

    if res == n:
        print(i)
        break
else:
    print(0)