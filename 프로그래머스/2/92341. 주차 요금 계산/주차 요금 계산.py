import math
from collections import defaultdict

def solution(fees, records):
    answer = []
    fee = []
    cars = defaultdict(list)

    for record in records:
        r = record.split(" ")
        cars[r[1]].append(r[0])

    for car in cars:
        if len(cars[car]) % 2 != 0:
            cars[car].append("23:59")

        cost = 0
        m = 0
        for i in range(0, len(cars[car]), 2):
            ih, im = cars[car][i].split(":")
            oh, om = cars[car][i + 1].split(":")
            m += (int(oh) - int(ih)) * 60 + int(om) - int(im)
        if m <= fees[0]:
            cost += fees[1]
        else:
            cost += fees[1]
            cost += math.ceil((m - fees[0])/fees[2]) * fees[3]
        fee.append((car, cost))

    for f in sorted(fee, key=lambda x: x[0]):
        answer.append(f[1])

    return answer