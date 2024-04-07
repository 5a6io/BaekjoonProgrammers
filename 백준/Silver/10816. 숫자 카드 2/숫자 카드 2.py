n = int(input())  #상근이가 가지고 있는 숫자 카드의 개수
cards = sorted(list(map(int, input().split())))  # 숫자 카드

m = int(input())  #상근이가 몇 개 가지고 있는 숫자 카드인지 구할 것.
targets = list(map(int, input().split())) #각 숫자

count = {}

for i in cards:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in targets:
    result = count.get(i)
    if result is None:
        print(0, end=' ')
    else:
        print(result, end=' ')