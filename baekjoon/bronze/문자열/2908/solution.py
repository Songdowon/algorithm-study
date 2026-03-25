# BOJ 2908 - 상수

import sys

input = sys.stdin.readline

#-------------------------
# solution 1. 문자열 뒤집기
#-------------------------

def solution_1(a, b):

    rev_a = int(a[::-1])
    rev_b = int(b[::-1])

    return max(rev_a, rev_b)

#-------------------------
# solution 2. reversed() 사용
#-------------------------

def solution_2(a, b):

    rev_a = int("".join(reversed(a)))
    rev_b = int("".join(reversed(b)))

    return rev_a if rev_a > rev_b else rev_b

#-------------------------
# solution 3. 숫자 연산
#-------------------------

def solution_3(a, b):

    a = int(a)
    b = int(b)

    rev_a = (a % 10) * 100 + ((a // 10) % 10) * 10 + (a // 100)
    rev_b = (b % 10) * 100 + ((b // 10) % 10) * 10 + (b // 100)

    return max(rev_a, rev_b)

#-------------------------
# main
#------------------------- 

def main():
    a, b = input().split()

    # 원하는 풀이 선택
    result = solution_1(a, b)

    print(result)

if __name__ == "__main__":
    main()