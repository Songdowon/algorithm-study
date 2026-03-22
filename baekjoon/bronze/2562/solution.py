# 2562 - 최댓값 + 위치 찾기

import sys

input = sys.stdin.readline

#-------------------------
# solution 1: max(), index() 사용
#-------------------------

data = []

for i in range(9):
    number = int(input())
    data.append(number)

print(max(data))
print(data.index(max(data))+1)


#-------------------------
# solution 2: enumerate() 사용
#-------------------------

numbers = [int(input()) for _ in range(9)]

max_value = 0
max_index = 0

for idx, value in enumerate(numbers, start=1):
    if value > max_value:
        max_value = value
        max_index = idx

print(max_value)
print(max_index)

#-------------------------
# solution 3: enumberate() + 축약버전
#-------------------------

numbers = [int(input()) for _ in range(9)]

max_index, max_value = max(enumerate(numbers, start=1), key=lambda x: x[1])
print(max_value)
print(max_index)