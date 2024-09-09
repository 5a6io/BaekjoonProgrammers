def alarm(h, m):
    if m - 45 < 0:
        h = (h - 1) % 24
    m = (m - 45) % 60

    print(h, m, sep=" ")


h, m = map(int, input().split())
alarm(h, m)