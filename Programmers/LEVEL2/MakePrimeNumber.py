# 26. 소수 만들기

'''에라토스테네스의 체(거의 다 내가 풀었는데...)'''
import math
from itertools import combinations

def is_prime_number(n):
    arr = [True for i in range(n + 1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(nums):
    answer = 0

    comb_lst = list(combinations(nums, 3))
    for pair in comb_lst:
        sum_pair = sum(pair)
        if is_prime_number(sum_pair):
            answer += 1

    return answer

nums_1 = [1, 2, 3, 4]
nums_2 = [1, 2, 7, 6, 4]

# print(solution(nums_1))
# print(solution(nums_2))

'''더 빠르고 좋은 풀이'''
def prime_number(n):
    answer = 0

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            answer += 1
    return 1 if answer == 1 else 0

def solution_best(nums):
    answer = sum([prime_number(sum(c)) for c in combinations(nums, 3)])

    return answer

print(solution_best(nums_1))
print(solution_best(nums_2))