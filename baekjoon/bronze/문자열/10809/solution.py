# BOJ 10809 - 알파벳 찾기

import sys

input = sys.stdin.readline

#-------------------------
# solution 1. find()
#-------------------------

def solution_1(word):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    result = []

    for ch in alphabet:
        result.append(word.find(ch))

    return result


#-------------------------
# solution 2. 리스트 + 직접 기록
#-------------------------

def solution_2(word):
    
    result = [-1] * 26

    for i, ch in enumerate(word):
        idx = ord(ch) - ord('a')
        
        if result[idx] == -1:
            result[idx] = i

    return result


#-------------------------
# solution 3. dictionary
#-------------------------

def solution_3(word):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    first_pos = {}

    for i, ch in enumerate(word):
        
        if ch not in first_pos:
            first_pos[ch] = i

    result = []

    for ch in alphabet:
        result.append(first_pos.get(ch, -1))

    return result

#-------------------------
# main
#-------------------------

def main():
    word = input().strip()

    #원하는 풀이 선택
    result = solution_1(word)
    
    print(*result)


if __name__ == "__main__":
    main()