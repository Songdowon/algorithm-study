# BOJ 2869 - 달팽이는 올라가고 싶다

import sys
input = sys.stdin.readline

#-------------------------
# solution 1: while문 - 내가 작성한 코드
#-------------------------

def solution1(a, b, v):

    height = 0
    day = 1

    while height < v:
        height += a
        if height >= v:
            break
        height -= b
        day += 1

    return day


#-------------------------
# solution 2: 마지막 날을 따로 생각하는 수학 풀이
#-------------------------

def solution2(a, b, v):

    day_gain = a - b
    return (v - a + day_gain - 1) // day_gain + 1


#-------------------------
# solution 3: 전체 높이에 대해 올림 계산 사용
#-------------------------

def solution3(a, b, v):

    return (v - b - 1) // (a - b) + 1


#-------------------------
# main
#-------------------------

def main():
    a, b, v = map(int, input().split())

    # 1, 2, 3 중 선택
    result = solution2(a, b, v)
    print(result)


if __name__ == "__main__":
    main()