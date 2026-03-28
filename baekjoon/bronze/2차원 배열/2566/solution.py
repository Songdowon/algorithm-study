# BOJ 2566 - 최댓값

import sys

input = sys.stdin.readline

#-------------------------
# solution 1. 이중 for문
#-------------------------

def solution_1(matrix):

    max_value = matrix[0][0]
    max_row = 0
    max_col = 0

    for i in range(9):
        for j in range(9):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_row = i
                max_col = j

    return max_value, max_row + 1, max_col + 1

#-------------------------
# solution 2. 리스트 펼치기
#-------------------------

def solution_2(matrix):

    flat = []
    
    for i in range(9):
        for j in range(9):
            flat.append((matrix[i][j], i + 1, j + 1))

    return max(flat) # 값이 같을 때 행 & 열 같이 비교함 

#-------------------------
# solution 3. max()와 index()
#-------------------------

def solution_3(matrix):

    max_value = max(map(max, matrix))

    for i in range(9):
        for j in range(9):
            if matrix[i][j] == max_value:
                return max_value, i + 1, j + 1

#-------------------------
# 출력 함수
#-------------------------

def print_result(max_value, row, col):
    print(max_value)
    print(row, col)

#-------------------------
# main
#-------------------------

def main():
    matrix = [list(map(int, input().split())) for _ in range(9)]

    # 원하는 풀이 선택
    max_value, row, col = solution_1(matrix)
    print_result(max_value, row, col)

if __name__ == "__main__":
    main()