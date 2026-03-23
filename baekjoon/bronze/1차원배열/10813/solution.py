# BOJ 10813 - 공 바꾸기

import sys

input = sys.stdin.readline

#-------------------------
# solution 1. swap
#-------------------------

def solution_1(n, operations):
    baskets = list(range(1, n + 1))

    for i, j in operations:
        baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]

    return baskets



#-------------------------
# solution 2. temporary storage
#-------------------------

def solution_2(n, operations):
    baskets = list(range(1, n + 1))

    for i, j in operations:
        a = baskets[i - 1]
        b = baskets[j - 1]

        baskets[i - 1] = b
        baskets[j - 1] = a

    return baskets

def main():
    n, m = map(int, input().split())
    operations = [tuple(map(int, input().split())) for _ in range(m)]

    # 1, 2 중 선택
    result = solution_1(n, operations)
    # result = solution_2(n, operations)
    print(*result)

main()
