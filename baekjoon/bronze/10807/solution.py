# BOJ 10807 - 개수 세기 

import sys
input = sys.stdin.readline

#-------------------------
# solution 1: count() 사용
#-------------------------

def solution1(nums, target):

    return nums.count(target)

#-------------------------
# solution 2: 직접 구현
#-------------------------

def solution2(n , nums, target):

    count = 0

    for i in range(n):
        if target == nums[i]:
            count += 1
    
    return count

#-------------------------
# main
#-------------------------

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())

    # 1, 2 중 선택

    result = solution2(n, nums, target)
    print(result)

main()

