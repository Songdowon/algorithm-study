# 10818 - 최소, 최대

import sys
input = sys.stdin.readline

#-------------------------
# solution 1: min/max 사용
#-------------------------

def solution1(nums):
    return min(nums), max(nums)

#-------------------------
# solution 2: 직접 구현
#-------------------------

def solution2(nums):
    min_val = nums[0]
    max_val = nums[0]

    for num in nums:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val. max_val


#-------------------------
# solution 3: map 활용 (메모리 절약)
#-------------------------
def solution3(nums):
    min_val = float('inf') # 양의 무한대(∞)
    max_val = float('-inf') # 음의 무한대(-∞)

    for num in nums:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val
#-------------------------
# main
#-------------------------

def main():
    n = int(input())

    mode = int(input())
    
    # 1, 2, 3 중 선택

    if mode == 1 or mode == 2:
        nums = list(map(int, input().split()))

        if mode == 1:
            answer = solution1(nums)
    
        else:
            answer = solution2(nums)
    
    else :
        nums = map(int, input().split())
        answer = solution3(nums)
    
    print(*answer)

main()