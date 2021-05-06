# 1. 멀쩡한 사각형

def gcd(x, y):
    if x < y:
        x, y = y, x
    else:
        while y:
            x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

import math

def solution(w, h):
    answer = w * h - (w + h - math.gcd(w, h))

    return answer

w_1 = 8
h_1 = 12

print(solution(w_1, h_1))

def GCD(x, y): return y if x == 0 else GCD(y % x, x)
def solution_best(w, h):
    answer = w * h - (w + h - GCD(w, h))

    return answer

print(solution_best(w_1, h_1))
