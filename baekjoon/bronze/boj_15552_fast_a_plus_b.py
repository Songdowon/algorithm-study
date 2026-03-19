# BOJ 15552 - 빠른 A+B

"""
문제 요약:
- 입력 개수가 많아 빠른 입출력이 필요한 문제

핵심 아이디어:
- input() 대신 sys.stdin.readline을 사용해 입력 속도를 개선

사용한 것:
- sys.stdin.readline
- 반복문
- map(int, input().split())

주의할 점:
- input() 사용 시 시간초과 가능
- sys.stdin.readline은 개행 문자를 포함할 수 있음

배운 점:
- Python에서는 입력 크기가 클 경우 빠른 입출력이 중요하다
"""

import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(a + b)