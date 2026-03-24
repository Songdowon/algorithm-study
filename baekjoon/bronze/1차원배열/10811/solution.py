# BoJ 10811 - 바구니 뒤집기

import sys

input = sys.stdin.readline

#-------------------------
# solution 1. slicing - my answer
#-------------------------

def solution_1(n, operations):

    basket = list(range(1, n+1))

    for i, j in operations:
        basket[i-1:j] = basket[i-1:j][::-1]

    return basket

#-------------------------
# solution 1. two-pointer swap - my answer
#-------------------------

def solution_1(n, operations):

    basket = list(range(1, n+1))

    for i, j in operations:
        left, right = i-1, j-1

        while left < right:
            basket[left], basket[right] = basket[right], basket[left]
            left += 1
            right -= 1

    return basket

#-------------------------
# solution 2. slicing 
#-------------------------

def solution_2(n, operations):

    basket = list(range(1, n+1))

    for i, j in operations:
        basket[i-1:j] = basket[i-1:j][::-1]

    return basket

#-------------------------
# solution 3. reversed() 
#-------------------------

def solution_3(n, operations):
    
    basket = list(range(1, n+1))

    for i, j in operations:
        basket[i-1:j] = list(reversed(basket[i-1:j]))

    return basket

#-------------------------
# solution 4. 직접 리스트 만들기
#-------------------------

def solution_4(n, operations):

    basket = list(range(1, n+1))

    for i, j in operations:
        temp = []
        for k in range(j-1, i-2, -1):
            temp.append(basket[k])
        basket[i-1:j] = temp

    return basket

#-------------------------
# main
#-------------------------

def main():
    n, m = map(int, input().split())
    operations = [tuple(map(int, input().split())) for _ in range(m)]

    # 원하는 풀이 선택
    result = solution_2(n, operations)

    print(*result)

if __name__ == "__main__":
    main()