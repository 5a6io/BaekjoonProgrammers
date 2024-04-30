T = int(input())

for test_case in range(1, T+1):
    a, b, c = map(int, input().split())

    if b-a != c-b:
        m = b * 2
        ac = a + c
        d = abs(m-ac)/2
        if (b+d)-a == c-(b+d):
            print("#"+str(test_case), str(d))
        elif (b-d)-a == c-(b-d):
            print("#" + str(test_case), str(d))
    else:
        print("#" + str(test_case), str(0.0))