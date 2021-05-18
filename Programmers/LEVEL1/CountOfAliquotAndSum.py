# 45. 약수의 개수와 덧셈

def solution(left, right):
    answer = 0

    for cost in range(left, right + 1):
        aliquot_cnt = 0
        for aliquot in range(1, cost + 1):
            if cost % aliquot == 0:
                aliquot_cnt += 1

        if aliquot_cnt % 2 == 0:
            answer += cost
        else:
            answer -= cost
    return answer

left_1 = 13
left_2 = 24

right_1 = 17
right_2 = 27

print(solution(left_1, right_1))
print(solution(left_2, right_2))

import math
def solution_other(left, right):
    answer = 0

    for cost in range(left, right + 1):
        sqrt = math.sqrt(cost)
        if int(sqrt) == sqrt:
            answer -= cost
        else:
            answer += cost

    return answer

print(solution_other(left_1, right_1))
print(solution_other(left_2, right_2))

def solution_best(left, right):
    answer = 0

    for cst in range(left, right + 1):
        if int(cst ** 0.5) == cst ** 0.5:
            answer -= cst
        else:
            answer += cst

    return answer

print(solution_best(left_1, right_1))
print(solution_best(left_2, right_2))