T = int(input())
num = {(2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4,
       (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9}

for tc in range(1, T + 1):
    N, M =  map(int, input().split())
    codes = list(set([input() for _ in range(N)])) # 중복되는 배열 제거
    ans = 0
    encoded = []
    for code in codes:
        decoded = format(int(code, 16), 'b').lstrip('0') # 1. 16진수 -> 2진수 변환
        p1, p2, p3 = 0, 0, 0
        odd, even, cnt = 0, 0, 0
        temp = ''
        for c in decoded:
            # 2. 비율에 맞는 번호 찾기
            if c == '1' and p2 == 0 and p3 == 0:
                p1 += 1
            elif c == '0' and p1 > 0 and p3 == 0:
                p2 += 1
            elif c == '1' and p1 > 0 and p2 > 0:
                p3 += 1
            elif p3 > 0:
                r = min(p1, p2, p3)
                new = num[(p1 // r, p2 // r, p3 // r)]
                temp += str(new)
                cnt += 1

                # 3. 코드 정상 여부
                if cnt == 8:
                    if (odd * 3 + even + new) % 10 == 0 and temp not in encoded:
                        ans += odd + even + new
                        encoded.append(temp)
                    odd = even = cnt = 0
                    temp = ''
                else:
                    if cnt % 2:
                        odd += new
                    else:
                        even += new

                p1 = p2 = p3 = 0

    print(f"#{tc} {ans}")