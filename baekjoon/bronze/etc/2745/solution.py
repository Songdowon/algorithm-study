# BOJ 2745 - 진법 변환

import sys
input = sys.stdin.readline

#-------------------------
# solution 1: 왼쪽부터 누적 계산 
#-------------------------

def solution1(n, b):

    result = 0

    for x in n:
        if x.isdigit():
            value = int(x)
        else:
            value = ord(x) - ord('A') + 10

        result = result * b + value

    return result


#-------------------------
# solution 2: 뒤에서부터 자리값 계산
#-------------------------

def solution2(n, b):

    result = 0
    power = 0

    for x in reversed(n):
        if x.isdigit():
            value = int(x)
        else:
            value = ord(x) - ord('A') + 10

        result += value * (b ** power)
        power += 1

    return result


#-------------------------
# solution 3: enumerate 활용
#-------------------------

def solution3(n, b):

    result = 0

    for i, x in enumerate(reversed(n)):
        if x.isdigit():
            value = int(x)
        else:
            value = ord(x) - ord('A') + 10

        result += value * (b ** i)

    return result


#-------------------------
# main
#-------------------------

def main():
    n, b = input().split()
    b = int(b)

    # 1, 2, 3 중 선택
    result = solution1(n, b)
    print(result)

if __name__ == "__main__":
    main()