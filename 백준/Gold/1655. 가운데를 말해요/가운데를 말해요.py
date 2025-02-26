import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input()) # 정수의 개수
left_nums = [] # 작은 수들 모임.
right_nums = [] # 큰 수들 모임.

for i in range(1, N+1):
    n = int(input())

    if len(left_nums) == len(right_nums):
        heappush(left_nums, -n)
    else:
        heappush(right_nums, n)
    
    # 길이가 짝수인 경우 루트 값을 비교하여 위치를 바꿈. 예를 들어 right의 루트가 2이고 left 루트가 -5(5)라면 이를 바꿔줌.
    if right_nums and -left_nums[0] > right_nums[0]:
        right = heappop(right_nums)
        left = heappop(left_nums)

        heappush(right_nums, -left)
        heappush(left_nums, -right)
    print(-left_nums[0])