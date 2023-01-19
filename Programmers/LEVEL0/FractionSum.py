# Restart 22. 분수의 덧셈

'''
Python Fraction module for operating Fraction
'''
from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    answer = []

    frac_1 = Fraction(numer1, denom1)
    frac_2 = Fraction(numer2, denom2)
    frac_sum = frac_1 + frac_2
    for num in [frac_sum.numerator, frac_sum.denominator]:
        answer.append(num)
    return answer

numer1_1 = 1
numer2_1 = 3

denom1_1 = 2
denom2_1 = 4

numer1_2 = 9
numer2_2 = 1

denom1_2 = 2
denom2_2 = 3

print(solution(numer1_1, denom1_1, numer2_1, denom2_1))
print(solution(numer1_2, denom1_2, numer2_2, denom2_2))