# 60. N개의 최소공배수

def solution(arr):
    answer = 0

    arr.sort(reverse = True)
    a, b = arr.pop(), arr.pop()
    while arr:
        n, m = max(a, b), min(a, b)
        while m > 0:
            n, m = m, n % m
        LCM = int(a * b / n)
        cst = arr.pop()
        a, b = max(LCM, cst), min(LCM, cst)
    n, m = max(a, b), min(a, b)
    while m > 0:
        n, m = m, n % m
    answer = int(a * b / n)

    return answer

arr_1 = [2, 6, 8, 14]
arr_2 = [1, 2, 3]

# print(solution(arr_1))
# print(solution(arr_2))

'''
math 모듈 사용하여 풀기
'''
import math
def solution_other(arr):
    answer = 0

    first = arr[0]
    for cst in arr[1:]:
        LCM = abs(first * cst) // math.gcd(first, cst)
        first = LCM

    answer = first
    return answer

# print(solution_other(arr_1))
# print(solution_other(arr_2))

'''
python 3.9 이상의 버전에서는 math모듈에서 lcm함수 지원
'''
# def solution_best(arr):
#     answer = math.lcm(3, 5)
#
#     return answer
# 
# print(solution_best(arr_1))
# print(solution_best(arr_2))