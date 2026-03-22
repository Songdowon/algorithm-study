# BOJ 10810 - 공 넣기

# 문제 요약 : i번부터 j번 바구니까지에 k번 번호가 적힌 공을 넣는다

import sys

input = sys.stdin.readline

def solution(n, operations):

    basket = [0] * n

    for i, j, k in operations:
        for idx in range(i-1, j):
            basket[idx] = k

    return basket

def main():
    n, m = map(int, input().split())
    operations = [tuple(map(int, input().split())) for _ in range(m)]

    result = solution(n, operations)
    print(*result)

main()

