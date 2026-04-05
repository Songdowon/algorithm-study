# BOJ 10798 - 세로읽기

import sys

input = sys.stdin.readline

#-------------------------
# solution 1. 이중 for문 (가장 많이 쓰이는 방식)
#-------------------------

def solution_1(words):

    result = []

    max_len = max(len(word) for word in words)

    for col in range(max_len):
        for row in range(5):
            if col < len(words[row]):
                result.append(words[row][col])

    return ''.join(result)

#-------------------------
# solution 2. list comprehension
#-------------------------

def solution_2(words):

    max_len = max(len(word) for word in words)

    return ''.join(
        words[row][col]
        for col in range(max_len)
        for row in range(5)
        if col < len(words[row])
    )

#-------------------------
# solution 3. 문자열 패딩 후 읽기
#-------------------------

def solution_3(words):

    max_len = max(len(word) for word in words)
    padded_words = [word.ljust(max_len) for word in words]

    result = []

    for col in range(max_len):
        for row in range(5):
            if padded_words[row][col] != ' ':
                result.append(padded_words[row][col])

    return ''.join(result)

#-------------------------
# main
#-------------------------

def main():
    words = [input().strip() for _ in range(5)]

    # 원하는 풀이 선택
    result = solution_1(words)
    print(result)

if __name__ == "__main__":
    main()