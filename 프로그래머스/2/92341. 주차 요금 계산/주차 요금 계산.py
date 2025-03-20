import math
from collections import defaultdict

def solution(fees, records):
    answer = []
    out_cars = defaultdict(int)
    in_cars = defaultdict(int)
    costs = []

    for record in records:
        time, num, io = record.split()
        h, m = map(int, time.split(":"))
        if io == "OUT":
            out_cars[num] += (h * 60 + m - in_cars[num])
            in_cars.pop(num)
        else:
            in_cars[num] = h * 60 + m

    for car in in_cars:
        out_cars[car] += (1439 - in_cars[car])

    for car in out_cars:
        if out_cars[car] <= fees[0]:
            costs.append((car, fees[1]))
        else:
            costs.append((car, fees[1] + math.ceil((out_cars[car] - fees[0]) / fees[2]) * fees[3]))

    for cost in sorted(costs, key=lambda x: x[0]):
        answer.append(cost[1])

    return answer