# BOJ 2738 - 행렬 덧셈

import sys

input = sys.stdin.readline

#-------------------------
# solution 1. 이중 for문 
#-------------------------

def solution_1(a, b, n, m):

    result = []

    for i in range(n):
        row = []
        for j in range(m):
            row.append(a[i][j] + b[i][j])
        result.append(row)

    return result

#-------------------------
# solution 2. list comprehension
#-------------------------

def solution_2(a, b, n, m):

    return [[a[i][j] + b[i][j] for j in range(m)] for i in range(n)]

#-------------------------
# solution 3. zip() 사용
#-------------------------

def solution_3(a, b):

    result = []

    for row_a, row_b in zip(a, b):
        result.append([x + y for x, y in zip(row_a, row_b)])

    return result

#-------------------------
# 출력 함수
#-------------------------

def print_matrix(matrix):

    for row in matrix:
        print(*row)

#-------------------------
# main
#-------------------------

def main():
    n, m = map(int, input().split())

    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]

    # 원하는 풀이 선택
    result = solution_1(a, b, n, m)
    print_matrix(result)


if __name__ == "__main__":
    main()