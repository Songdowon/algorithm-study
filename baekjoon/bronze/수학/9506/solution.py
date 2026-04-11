# BOJ 9506 - 약수들의 합

import sys
input = sys.stdin.readline

#-------------------------
# solution 1: join 사용
#-------------------------

def solution1(n):

    divisors = []
    total = 0

    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
            total += i

    if total == n:
        return f"{n} = {' + '.join(map(str, divisors))}"
    else:
        return f"{n} is NOT perfect."


#-------------------------
# solution 2: 마지막 원소를 조건문으로 처리
#-------------------------

def solution2(n):

    divisors = []
    total = 0

    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
            total += i

    if total == n:
        result = f"{n} = "

        for i in range(len(divisors)):
            if i == len(divisors) - 1:
                result += str(divisors[i])
            else:
                result += str(divisors[i]) + " + "

        return result
    else:
        return f"{n} is NOT perfect."


#-------------------------
# solution 3: 슬라이싱 사용
#-------------------------

def solution3(n):

    divisors = []
    total = 0

    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
            total += i

    if total == n:
        result = f"{n} = "

        for x in divisors[:-1]:
            result += str(x) + " + "

        result += str(divisors[-1])

        return result
    else:
        return f"{n} is NOT perfect."


#-------------------------
# main
#-------------------------

def main():
    while True:
        n = int(input())

        if n == -1:
            break

        # 1, 2, 3 중 선택
        result = solution2(n)
        print(result)


if __name__ == "__main__":
    main()