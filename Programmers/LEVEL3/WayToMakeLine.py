# 4. 줄 서는 방법

import math
def solution(n, k):
    answer = []

    num_lst = [i for i in range(1, n + 1)]
    while n != 0:
        temp = math.factorial(n) // n
        idx = k // temp
        k = k % temp
        if k == 0:
            answer.append(num_lst.pop(idx - 1))
        else:
            answer.append(num_lst.pop(idx))

        n -= 1
    return answer

n_1 = 3

k_1 = 5

print(solution(n_1, k_1))

'''
accuracy : 63.2, efficiency : 0
n이 20이하의 자연수라서 permutations 사용 시 시간초과 발생
'''
from itertools import permutations
def solution_mine(n, k):
    answer = []

    line_cases = list(permutations(range(1, n + 1), n))
    for i in range(len(line_cases)):
        if i == k - 1:
            answer += line_cases[i]
    return answer

print(solution_mine(n_1, k_1))

def solution_best(n, k):
    answer = []

    order = list(range(1, n + 1))
    while n != 0:
        fact = math.factorial(n - 1)
        answer.append(order.pop((k - 1) // fact))
        n, k = n - 1, k % fact
        
    return answer

print(solution_best(n_1, k_1))