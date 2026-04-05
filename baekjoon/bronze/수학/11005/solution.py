# BOJ 11005 - 진법 변환 2

import sys
input = sys.stdin.readline

#-------------------------
# solution 1: 나머지를 문자열에 앞에 붙이기
#-------------------------

def solution1(n, b):

    result = ""

    while n > 0:
        remainder = n % b

        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(remainder - 10 + ord('A')) + result

        n //= b

    return result


#-------------------------
# solution 2: 리스트에 저장 후 뒤집기
#-------------------------

def solution2(n, b):

    result = []

    while n > 0:
        remainder = n % b

        if remainder < 10:
            result.append(str(remainder))
        else:
            result.append(chr(remainder - 10 + ord('A')))

        n //= b

    return ''.join(reversed(result))


#-------------------------
# solution 3: 숫자 테이블 활용
#-------------------------

def solution3(n, b):

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []

    while n > 0:
        remainder = n % b
        result.append(digits[remainder])
        n //= b

    return ''.join(reversed(result))


#-------------------------
# main
#-------------------------

def main():
    n, b = map(int, input().split())

    # 1, 2, 3 중 선택
    result = solution1(n, b)
    print(result)

if __name__ == "__main__":
    main()