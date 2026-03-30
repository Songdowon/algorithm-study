# BOJ 2563 - 색종이

import sys

input = sys.stdin.readline

#-------------------------
# solution 1. 2차원 배열에 표시
#-------------------------

def solution_1(papers):

    board = [[0] * 100 for _ in range(100)]

    for x, y in papers:
        for row in range(y, y + 10):
            for col in range(x, x + 10):
                board[row][col] = 1

    result = 0

    for row in board:
        result += sum(row)

    return result

#-------------------------
# solution 2. set으로 좌표 저장
#-------------------------

def solution_2(papers):

    covered = set()

    for x, y in papers:
        for row in range(y, y + 10):
            for col in range(x, x + 10):
                covered.add((row, col))

    return len(covered)

#-------------------------
# solution 3. 2차원 배열 + 전체 합 한 번에 계산
#-------------------------

def solution_3(papers):

    board = [[0] * 100 for _ in range(100)]

    for x, y in papers:
        for row in range(y, y + 10):
            for col in range(x, x + 10):
                board[row][col] = 1

    return sum(sum(row) for row in board)

#-------------------------
# main
#-------------------------

def main():
    n = int(input())
    papers = [tuple(map(int, input().split())) for _ in range(n)]

    # 원하는 풀이 선택
    result = solution_1(papers)
    print(result)

if __name__ == "__main__":
    main()