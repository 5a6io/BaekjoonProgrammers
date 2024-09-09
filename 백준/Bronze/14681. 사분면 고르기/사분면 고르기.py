def find_quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 < y:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4


x = int(input())
y = int(input())

print(find_quadrant(x, y))