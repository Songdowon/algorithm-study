# BOJ 3052 - 나머지

import sys

input = sys.stdin.readline

#-------------------------
# solution 1. if문 - my answer
#-------------------------

def solution_1(numbers):
    
    remainders =  []

    for num in numbers:
        r = num % 42
        if r not in remainders:
            remainders.append(r)

    return len(remainders)

#-------------------------
# solution 2. set comprehension
#-------------------------

def solution_2(numbers):
    
    return len({num % 42} for num in numbers)

#-------------------------
# solution 3. list → set 변환
#-------------------------

def solution_3(numbers):

    remainders = []

    for num in numbers:
        remainders.append(num % 42)

    return len(set(remainders))

#-------------------------
# solution 4. boolean 배열 
#-------------------------

def solution_4(numbers):

    check = [False] * 42

    for num in numbers:
        check[num % 42] = True

    return sum(check)


#-------------------------
# main
#-------------------------

def main():
    numbers = [int(input()) for _ in range(10)]
    
    # 원하는 풀이 선택
    result = solution_2(numbers)
    print(result)


if __name__ == "__main__" :
    main()