# BOJ 2720 - 세탁소 사장 동혁

import sys
input = sys.stdin.readline

#-------------------------
# solution 1: 나눗셈과 나머지 직접 갱신
#-------------------------

def solution1(c):

    quarter = c // 25
    c %= 25

    dime = c // 10
    c %= 10

    nickel = c // 5
    c %= 5

    penny = c

    return quarter, dime, nickel, penny


#-------------------------
# solution 2: 동전 배열 순회
#-------------------------

def solution2(c):

    coins = [25, 10, 5, 1]
    result = []

    for coin in coins:
        result.append(c // coin)
        c %= coin

    return tuple(result)


#-------------------------
# solution 3: divmod 활용
#-------------------------

def solution3(c):

    quarter, c = divmod(c, 25)
    dime, c = divmod(c, 10)
    nickel, c = divmod(c, 5)
    penny = c

    return quarter, dime, nickel, penny


#-------------------------
# main
#-------------------------

def main():
    t = int(input())

    for _ in range(t):
        c = int(input())

        # 1, 2, 3 중 선택
        quarter, dime, nickel, penny = solution1(c)
        print(quarter, dime, nickel, penny)


if __name__ == "__main__":
    main()