# 15. 소수 찾기

from itertools import permutations
def solution(numbers):
    answer_set = set()

    for i in range(len(numbers)):
        answer_set |= set(map(int, map(''.join, permutations(
            list(numbers), i + 1))))
    answer_set -= set(range(0, 2))

    for i in range(2, int(max(answer_set) ** 0.5) + 1):
        answer_set -= set(range(i * 2, max(answer_set) + 1, i))
    answer = len(answer_set)
    return answer

numbers_1 = '17'
numbers_2 = '011'

print(solution(numbers_1))
print(solution(numbers_2))

import math

def is_prime(n):
    k = math.sqrt(n)

    if n < 2:
        return False

    for i in range(2, int(k) + 1):
        if n % i == 0:
            return False
    return True

def solution_best(numbers):
    answer = []

    for k in range(1, len(numbers) + 1):
        per_lst = list(map(''.join, permutations(list(numbers), k)))
        for i in list(set(per_lst)):
            answer.append(int(i))

    answer = len((set(answer)))
    return answer

print(solution_best(numbers_1))
print(solution_best(numbers_2))