# BOJ 1157 - 단어 공부

import sys

input = sys.stdin.readline

#-------------------------
# solution 1. dictionary counting - my answer
#-------------------------

def solution_1(word):

    count = {}

    for ch in word:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    max_count = max(count.values())

    candidates = []

    for ch, freq in count.items():
        if freq == max_count:
            candidates.append(ch)

    if len(candidates) > 1:
        return '?'
    return candidates[0]


#-------------------------
# solution 2. set + count()
#-------------------------

def solution_2(word):

    max_count = 0
    answer = '?'

    for ch in set(word):
        freq = word.count(ch)

        if freq > max_count:
            max_count = freq
            answer = ch
        elif freq == max_count:
            answer = '?'

    return answer


#-------------------------
# solution 3. list counting (A-Z)
#-------------------------

def solution_3(word):

    counts = [0] * 26

    for ch in word:
        counts[ord(ch) - ord('A')] += 1

    max_count = max(counts)

    if counts.count(max_count) > 1:
        return '?'

    return chr(counts.index(max_count) + ord('A'))


#-------------------------
# solution 4. Counter
#-------------------------

from collections import Counter

def solution_4(word):

    counter = Counter(word)
    common = counter.most_common()

    if len(common) > 1 and common[0][1] == common[1][1]:
        return '?'

    return common[0][0]


#-------------------------
# main
#-------------------------

def main():
    word = input().strip().upper()

    # 원하는 풀이 선택
    result = solution_1(word)

    print(result)


if __name__ == "__main__":
    main()