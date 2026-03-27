# BOJ 2444 - 별 찍기 - 7

#-------------------------
# solution 1: 문자열 곱 (가장 표준)
#-------------------------

def solution1(n):
    
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))


#-------------------------
# solution 2: 중심 기준 (대칭 사고)
#-------------------------

def solution2(n):
    
    for i in range(2 * n - 1):
        
        dist = abs(n - 1 - i)
        stars = 2 * (n - dist) - 1
        spaces = dist
        print(' ' * spaces + '*' * stars)


#-------------------------
# solution 3: 리스트 모아서 출력 (빠른 출력)
#-------------------------
def solution3(n):
    
    result = []

    for i in range(1, n + 1):
        result.append(' ' * (n - i) + '*' * (2 * i - 1))
    
    for i in range(n - 1, 0, -1):
        result.append(' ' * (n - i) + '*' * (2 * i - 1))

    print('\n'.join(result))


#-------------------------
# main
#-------------------------
def main():
    
    n = int(input())

    # 선택
    mode = int(input())  # 1, 2, 3

    if mode == 1:
        solution1(n)
    elif mode == 2:
        solution2(n)
    else:
        solution3(n)

if __name__ == "__main__":
    main()