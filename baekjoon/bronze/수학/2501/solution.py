# BOJ 2501 - 약수 구하기

import sys
input = sys.stdin.readline

#-------------------------
# solution 1: for문으로 약수 직접 찾기
#-------------------------

def solution1(n, k):

    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    if len(divisors) >= k:
        return divisors[k - 1]
    else:
        return 0


#-------------------------
# solution 2: 약수를 찾으면서 k번째가 나오면 바로 종료
#-------------------------

def solution2(n, k):

    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
            if count == k:
                return i

    return 0


#-------------------------
# solution 3: 리스트 컴프리헨션 사용
#-------------------------

def solution3(n, k):

    divisors = [i for i in range(1, n + 1) if n % i == 0]

    return divisors[k - 1] if len(divisors) >= k else 0


#-------------------------
# main
#-------------------------

def main():
    n, k = map(int, input().split())

    # 1, 2, 3 중 선택
    result = solution2(n, k)
    print(result)


if __name__ == "__main__":
    main()