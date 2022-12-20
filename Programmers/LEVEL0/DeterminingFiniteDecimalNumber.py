# Restart 18.유한소수 구하기

'''
Try to find aliquots in b that are divided by GCD.
'''
from math import gcd, sqrt
def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

def solution(a, b):
    answer = 0

    a, b = a // gcd(a, b), b // gcd(a, b)

    b_aliquots = [b_aliq for b_aliq in range(2, b + 1) if b % b_aliq == 0]
    b_aliquot_primes = [b_aliquot for b_aliquot in b_aliquots if is_prime(b_aliquot)]
    answer_lst = [b_aliquot_prime for b_aliquot_prime in b_aliquot_primes if b_aliquot_prime != 2 and
                  b_aliquot_prime != 5]

    answer = 1 if len(answer_lst) == 0 else 2
    return answer

a_1 = 7
a_2 = 11
a_3 = 12

b_1 = 20
b_2 = 22
b_3 = 21

print(solution(a_1, b_1))
print(solution(a_2, b_2))
print(solution(a_3, b_3))

'''
Best idea : just divide 2 and 5 and if there exist rest, judge it.
'''
def solution_best(a, b):
    answer = 0

    b //= gcd(a, b)
    while b % 2 == 0:
        b //= 2

    while b % 5 == 0:
        b //= 5
    answer = 1 if b == 1 else 2

    return answer

a_1 = 7
a_2 = 11
a_3 = 12

b_1 = 20
b_2 = 22
b_3 = 21

print(solution_best(a_1, b_1))
print(solution_best(a_2, b_2))
print(solution_best(a_3, b_3))