# Restart 9. 구슬 나누는 경우의 수

# My Solution
def solution(balls, share):
    answer = 0

    n_factorial, m_factorial, n_diff_m_factorial = 1, 1, 1
    for n_facto in range(1, balls + 1):
        n_factorial *= n_facto

    for m_facto in range(1, share + 1):
        m_factorial *= m_facto

    for n_dif_m_facto in range(1, balls - share + 1):
        n_diff_m_factorial *= n_dif_m_facto

    answer = n_factorial / ((n_diff_m_factorial) * m_factorial)
    return answer

balls_1 = 3
balls_2 = 5

share_1 = 2
share_2 = 3

print(solution(balls_1, share_1))
print(solution(balls_2, share_2))

import math
def solution_other(balls, share):
    answer = math.comb(balls, share)

    return answer

print(solution_other(balls_1, share_1))
print(solution_other(balls_2, share_2))