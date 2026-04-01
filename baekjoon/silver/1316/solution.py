# BOJ 1316 - 그룹 단어 체커

import sys

input = sys.stdin.readline

#-------------------------
# solution 1. 가장 기본적이고 많이 쓰는 풀이
# 이전 문자와 현재 문자를 비교
#-------------------------

def solution_1(words):

    count = 0

    for word in words:
        seen = set()
        prev = ""

        is_group_word = True

        for char in word:
            if char != prev:
                if char in seen:
                    is_group_word = False
                    break
                seen.add(char)
            prev = char

        if is_group_word:
            count += 1

    return count

#-------------------------
# solution 2. 문자열 슬라이싱 활용
# 현재 문자가 이전까지 등장했는지 확인
#-------------------------

def solution_2(words):

    count = 0

    for word in words:
        is_group_word = True

        for i in range(1, len(word)):
            if word[i] != word[i - 1] and word[i] in word[:i]:
                is_group_word = False
                break

        if is_group_word:
            count += 1

    return count

#-------------------------
# solution 3. 중복 제거 순서 비교
#-------------------------

def solution_3(words):

    count = 0

    for word in words:
        compressed = []

        for char in word:
            if not compressed or compressed[-1] != char:
                compressed.append(char)

        if len(compressed) == len(set(compressed)):
            count += 1

    return count

#-------------------------
# main
#-------------------------

def main():
    n = int(input())
    words = [input().strip() for _ in range(n)]

    # 원하는 풀이 선택
    result = solution_1(words)
    print(result)

if __name__ == "__main__":
    main()