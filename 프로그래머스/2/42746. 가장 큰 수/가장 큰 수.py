def solution(numbers):
    numbers_list = [str(num) for num in numbers]
    numbers_list.sort(key=lambda x:x*3, reverse=True)

    answer = str(int(''.join(numbers_list)))
    return answer