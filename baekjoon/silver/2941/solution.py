# BOJ 2941 - 크로아티아 알파벳

import sys

input = sys.stdin.readline

#-------------------------
# solution 1. replace()로 크로아티아 알파벳 치환
#-------------------------

def solution_1(word):

    croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

    for alpha in croatia:
        word = word.replace(alpha, "*")

    return len(word)

#-------------------------
# solution 2. 직접 탐색
#-------------------------

def solution_2(word):

    croatia = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="}

    count = 0
    i = 0

    while i < len(word):
        if i + 3 <= len(word) and word[i:i+3] in croatia:
            count += 1
            i += 3
        elif i + 2 <= len(word) and word[i:i+2] in croatia:
            count += 1
            i += 2
        else:
            count += 1
            i += 1

    return count

#-------------------------
# solution 3. 직접 탐색 + 조건문
#-------------------------

def solution_3(word):

    count = 0
    i = 0

    while i < len(word):
        if word[i:i+3] == "dz=":
            count += 1
            i += 3
        elif word[i:i+2] in ["c=", "c-", "d-", "lj", "nj", "s=", "z="]:
            count += 1
            i += 2
        else:
            count += 1
            i += 1

    return count

#-------------------------
# main
#-------------------------

def main():
    word = input().strip()

    # 원하는 풀이 선택
    result = solution_1(word)
    print(result)

if __name__ == "__main__":
    main()