# BOJ 2903 - 중앙 이동 알고리즘

import sys
input = sys.stdin.readline

#-------------------------
# solution 1: 한 변의 점 개수 공식 사용
#-------------------------

def solution1(n):

    side = 2 ** n + 1
    return side ** 2


#-------------------------
# solution 2: 반복적으로 한 변의 점 개수 갱신
#-------------------------

def solution2(n):

    side = 2

    for _ in range(n):
        side = side * 2 - 1

    return side ** 2


#-------------------------
# solution 3: 점화식 활용
#-------------------------

def solution3(n):

    points = 4

    for _ in range(n):
        side = int(points ** 0.5)
        new_side = side * 2 - 1
        points = new_side ** 2

    return points


#-------------------------
# main
#-------------------------

def main():
    n = int(input())

    # 1, 2, 3 중 선택
    result = solution1(n)
    print(result)

if __name__ == "__main__":
    main()