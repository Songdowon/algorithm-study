# BOJ 15552 - 빠른 A+B

"""
문제:
입력 개수가 많아서 빠른 입출력 필요

접근:
sys.stdin.readline 사용 

시간복잡도:
O(N)

배운 점:
input()보다 빠른 입출력 필요
"""

import sys

input = sys.stdin.readline

number = int(input())

for _ in range(number):
    a, b = map(int, input().split())
    print(a + b)