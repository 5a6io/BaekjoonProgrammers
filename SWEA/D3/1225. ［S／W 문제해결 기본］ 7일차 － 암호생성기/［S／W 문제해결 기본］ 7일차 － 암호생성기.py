for i in range(10):
    t = int(input())
    codes = list(map(int, input().split()))

    sub = 1
    while True:
        if sub > 5:
            sub = 1
        cur = codes.pop(0) - sub
        if cur <= 0:
            codes.append(0)
            break
        codes.append(cur)
        sub += 1


    print("#{} {} {} {} {} {} {} {} {}".format(t, *codes))