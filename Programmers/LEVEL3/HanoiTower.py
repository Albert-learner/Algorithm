# 3. 하노이의 탑

def hanoi(n, start, end, mid, answer):
    if n == 1:
        answer.append([start, end])
        return

    hanoi(n - 1, start, mid, end, answer)
    answer.append([start, end])
    hanoi(n - 1, mid, end, start, answer)

def solution(n):
    answer = []

    hanoi(n, 1, 3, 2, answer)
    return answer

n_1 = 2

print(solution(n_1))

'''
런타임 오류
'''
from itertools import combinations
def solution_mine(n):
    answer = [[]]

    hanoi_cases = 2 ** n - 1
    for x, y in list(combinations(range(1, hanoi_cases + 1), n)):
        answer.append([x, y])
    return answer

# print(solution_mine(n_1))

def solution_best(n, start = 1, end = 3, mid = 2):
    if n == 1:
        return ([[start, end]])

    return solution_best(n - 1, start, mid, end) + [[start, end]] + solution_best(n - 1, mid, end, start)

# print(solution_best(n_1))