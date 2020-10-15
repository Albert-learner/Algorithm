# 34. 최대공약수와 최소공배수

# 좀만 더 생각하지...
def solution(n, m):
    answer = []

    a, b = max(n, m), min(n, m)
    t = 1
    while t > 0:
        t = a % b
        a, b = b, t
    answer = [a, int(n * m / a)]
    return answer

n_1 = 3
n_2 = 2

m_1 = 12
m_2 = 5

print(solution(n_1, m_1))
print(solution(n_2, m_2))

from math import gcd

def solution_best(n, m):
    answer = []

    GCD = gcd(n, m)
    LCM = n * m // GCD

    answer.append(GCD)
    answer.append(LCM)

    return answer

print(solution_best(n_1, m_1))
print(solution_best(n_2, m_2))