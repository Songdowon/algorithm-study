# BOJ 1193 - 분수찾기

import sys

input = sys.stdin.readline

#-------------------------
# solution 1. 가장 기본적이고 많이 쓰는 풀이
# 대각선(구간) 기준으로 접근
#-------------------------

def solution_1(x):

    line = 1

    while x > line:
        x -= line
        line += 1

    if line % 2 == 0:
        numerator = x
        denominator = line - x + 1
    else:
        numerator = line - x + 1
        denominator = x

    return f"{numerator}/{denominator}"

#-------------------------
# solution 2. 누적합으로 구간 찾기
# x가 몇 번째 대각선에 속하는지 확인
#-------------------------

def solution_2(x):

    line = 1
    end = 1

    while x > end:
        line += 1
        end += line

    start = end - line + 1
    offset = x - start

    if line % 2 == 0:
        numerator = 1 + offset
        denominator = line - offset
    else:
        numerator = line - offset
        denominator = 1 + offset

    return f"{numerator}/{denominator}"

#-------------------------
# solution 3. 수학적으로 대각선 찾기
# 1 + 2 + ... + n >= x 를 만족하는 최소 n
#-------------------------

def solution_3(x):

    line = 1

    while line * (line + 1) // 2 < x:
        line += 1

    prev_end = line * (line - 1) // 2
    offset = x - prev_end

    if line % 2 == 0:
        numerator = offset
        denominator = line - offset + 1
    else:
        numerator = line - offset + 1
        denominator = offset

    return f"{numerator}/{denominator}"

#-------------------------
# main
#-------------------------

def main():
    x = int(input().strip())

    # 원하는 풀이 선택
    result = solution_1(x)
    print(result)

if __name__ == "__main__":
    main()