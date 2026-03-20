# BOJ 15552 - 빠른 입력

import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(a + b)
