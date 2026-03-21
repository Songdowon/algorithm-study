# BOJ 10807 - 개수 세기 

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

print(arr.count(target))

