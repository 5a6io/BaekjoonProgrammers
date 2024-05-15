for test_case in range(1, 11):
    n = int(input())
    boxes = list(map(int, input().split()))
    answer = 0

    for i in range(n):
        if max(boxes) - min(boxes) == 1 or max(boxes) - min(boxes) == 0:
            break
        mx = max(boxes)
        mn = min(boxes)

        boxes[boxes.index(mx)] -= 1
        boxes[boxes.index(mn)] += 1

        answer = max(boxes) - min(boxes)

    print(f"#{test_case} {answer}")