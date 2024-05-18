N, C = map(int, input().split())

home = [int(input()) for _ in range(N)]

home.sort()

s = 1 # 공유기 최소 거리
e = home[-1] - home[0] # 공유기 최대 거리
answer = 0

while s <= e:
    mid = (s+e) // 2
    now = home[0]
    cnt = 1

    for i in home:
        if i >= now + mid:
            cnt += 1
            now = i

    if cnt >= C:
        s = mid + 1
        answer = mid
    else:
        e = mid - 1

print(answer)