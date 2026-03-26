# BOJ 5622 - 다이얼

import sys

input = sys.stdin.readline

#-------------------------
# solution 1. group 문자열 순회 - my answer
#-------------------------

def solution_1(word):
    
    groups = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    
    total = 0

    for ch in word:
        for i, group in enumerate(groups):
            if ch in group:
                total += i + 3
                break

    return total


#-------------------------
# solution 2. dictionary
#-------------------------

def solution_2(word):
    
    dial = {
        'A': 3, 'B': 3, 'C': 3,
        'D': 4, 'E': 4, 'F': 4,
        'G': 5, 'H': 5, 'I': 5,
        'J': 6, 'K': 6, 'L': 6,
        'M': 7, 'N': 7, 'O': 7,
        'P': 8, 'Q': 8, 'R': 8, 'S': 8,
        'T': 9, 'U': 9, 'V': 9,
        'W': 10, 'X': 10, 'Y': 10, 'Z': 10
    }
    
    total = 0

    for ch in word:
        total += dial[ch]

    return total


#-------------------------
# solution 3. ord() 범위 처리
#-------------------------

def solution_3(word):
    
    total = 0

    for ch in word:
        if 'A' <= ch <= 'C':
            total += 3
        elif 'D' <= ch <= 'F':
            total += 4
        elif 'G' <= ch <= 'I':
            total += 5
        elif 'J' <= ch <= 'L':
            total += 6
        elif 'M' <= ch <= 'O':
            total += 7
        elif 'P' <= ch <= 'S':
            total += 8
        elif 'T' <= ch <= 'V':
            total += 9
        else:  # WXYZ
            total += 10

    return total

#-------------------------
# solution 4. 문자열 압축 매핑
#-------------------------

def solution_4(word):

    dial = "2223334445556667777888999"

    total = 0

    for ch in word:
        total += int(dial[ord(ch) - ord('A')]) + 1

    return total


#-------------------------
# main
#-------------------------

def main():
    word = input().strip()

    # 원하는 풀이 선택
    result = solution_2(word)

    print(result)


if __name__ == "__main__":
    main()