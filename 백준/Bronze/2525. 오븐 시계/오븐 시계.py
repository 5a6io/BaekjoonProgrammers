def alarm(h, m, t):
    i = (m + t) // 60
    h = (h + i) % 24
    m = (m + t) % 60

    print(h, m, sep=" ")


h, m = map(int, input().split())
t = int(input())

alarm(h, m, t)