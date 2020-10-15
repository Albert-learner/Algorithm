# 32. 정수 제곱근 판별

def solution(n):
    answer = 0

    n_root = n ** 0.5
    if int(n_root) == n_root:
        answer = int((n_root + 1) ** 2)
    else:
        answer = -1
    return answer

n_1 = 121
n_2 = 3

print(solution(n_1))
print(solution(n_2))

import math

def solution_best(n):
    answer = 0

    if math.sqrt(n).is_integer():
        answer = int(pow(math.sqrt(n) + 1, 2))
    else:
        answer = -1
    return answer

# print(solution_best(n_1))
# print(solution_best(n_2))