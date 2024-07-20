a, b, c, d, e, f = map(int, input().split())

det = a * e - b * d
x, y = (e * c - b * f)//det, (- d * c + a * f)//det

print(x, y, sep=' ')