# 5. 멀리 뛰기


def solution(n):
    answer = 0

    if n < 3:
        return n

    cases = [0] * (n + 1)
    cases[1], cases[2] = 1, 2
    for i in range(3, n + 1):
        cases[i] = cases[i - 1] + cases[i - 2]

    answer = cases[n] % 1234567
    return answer

n_1 = 4
n_2 = 3

print(solution(n_1))
print(solution(n_2))

'''
2000이하의 정수여도 각 case 하나에 대해 permutation을 사용
'''
from itertools import permutations
def solution_mine(n):
    answer = 1

    q, r = divmod(n, 2)
    cases = [[1] * n]
    two_cnts = q
    for two_cnt in range(1, two_cnts + 1):
        one_cnts = n - (2 * two_cnt)
        case = [2] * two_cnt + [1] * one_cnts
        cases.append(case)

    for case in cases[1:]:
        perm_case = len(list(set(list(permutations(case, len(case))))))
        answer += perm_case
    return answer

# print(solution_mine(n_1))
# print(solution_mine(n_2))

'''
같은 피보나치수열인데 한 줄만에 품
'''
def solution_best(n):
    return 1 if n < 2 else solution_best(n - 1) + solution_best(n - 2)

print(solution_best(n_1))
print(solution_best(n_2))