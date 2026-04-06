# BOJ 2292 - 벌집

import sys
input = sys.stdin.readline

#-------------------------
# solution 1: 규칙 직접 누적
#-------------------------
def solution1(n):
    layer = 1
    max_room = 1

    while n > max_room:
        max_room += 6 * layer
        layer += 1

    return layer

#-------------------------
# solution 2: 현재 범위 갱신
#-------------------------
def solution2(n):
    count = 1
    end = 1

    while end < n:
        end += 6 * count
        count += 1

    return count

#-------------------------
# solution 3: 시작값에서 확장
#-------------------------
def solution3(n):
    if n == 1:
        return 1

    room = 1
    answer = 1

    while room < n:
        room += 6 * answer
        answer += 1

    return answer

#-------------------------
# main
#-------------------------
def main():
    n = int(input())

    # 1, 2, 3 중 선택
    print(solution1(n))

if __name__ == "__main__":
    main()