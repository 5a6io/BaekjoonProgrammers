def solution(arr, divisor):
    return sorted([a for a in arr if a%divisor == 0]) or [-1]