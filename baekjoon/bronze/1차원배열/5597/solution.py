# BOJ 5597 - 과제 안 내신 분..? 

import sys

input = sys.stdin.readline

#-------------------------
# solution 1. remove() - my answer
#-------------------------

def solution_1(submitted):

    students = list(range(1, 31))

    for student in submitted:
        students.remove(student)

    return students

#-------------------------
# solution 2. set 
#-------------------------

def solution_2(submitted):

    submitted = set(submitted)
    result = []

    for i in range(1, 31):
        if i not in submitted:
            result.append(i)

    return result

#-------------------------
# solution 3. set - set 
#-------------------------

def solution_3(submitted):
    
    students = set(range(1, 31))
    submitted = set(submitted)

    return sorted(students - submitted)

#-------------------------
# solution 4. boolean 배열
#-------------------------

def solution_4(submitted):

    check = [False] * 31

    for student in submitted:
        check[student] = True

    result = []
    for i in range(1, 31):
        if not check[i]:
            result.append(i)

    return result

def main():
    submitted = [int(input()) for _ in range(28)]

    # 원하는 풀이 선택
    result = solution_4(submitted)

    print(*result, sep="\n")

main()