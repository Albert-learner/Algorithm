# 12. 2 x n 타일링

'''
피보나치 수열
'''
def solution(n):
    answer = 0

    cases = [1, 2]
    for i in range(2, n):
        cases.append((cases[-1] + cases[-2]) % 1000000007)

    answer = cases[-1]
    return answer

n_1 = 4

print(solution(n_1))

def solution_other(n):
    answer = 0

    a, b = 1, 1
    for i in range(1, n):
        a, b = b, (a + b) % 1000000007

    answer = b
    return answer

# print(solution_other(n_1))

from functools import reduce

solution_best = lambda n : reduce(lambda a, _ : (a[1] % 1000000007, sum(a) % 1000000007),
                                  range(1, n), [1, 1])[1]

# print(solution_best(n_1))