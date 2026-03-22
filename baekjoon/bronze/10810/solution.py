# BOJ 10810 - 공 넣기

# 문제 요약 : i번부터 j번 바구니까지에 k번 번호가 적힌 공을 넣는다

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

basket = [0]*n

for _ in range(m):
    i, j, k = map(int, input().split())
    for i in range(i-1, j):
        basket[i] = k

print(*basket)


