# 13. 두 정수 사이의 합

def solution(a, b):
    answer = 0

    if a > b:
        answer += b
        for i in range(b + 1, a + 1):
            answer += i
    elif a == b:
        answer += a
    else:
        answer += a
        for i in range(a + 1, b + 1):
            answer += i

    return answer

a_1, b_1 = 3, 5
a_2, b_2 = 3, 3
a_3, b_3 = 5, 3

# print(solution(a_1, b_1))
# print(solution(a_2, b_2))
# print(solution(a_3, b_3))

def solution_notgood(a, b):
    answer = 0

    if a > b:
        answer = b
        for i in range(a - b):
            answer += b + i + 1
    elif a < b:
        answer = a
        for i in range(b - a):
            answer += a + i + 1
    else:
        answer = a

    return answer

# print(solution_notgood(a_1, b_1))
# print(solution_notgood(a_2, b_2))
# print(solution_notgood(a_3, b_3))

def solution_best(a, b):
    answer = (abs(a-b)+1)*(a+b)//2

    return answer

print(solution_best(a_1, b_1))
print(solution_best(a_2, b_2))
print(solution_best(a_3, b_3))

def solution_other1(a, b):
    answer = 0

    if a > b:
        a, b = b, a

    answer = sum(range(a, b + 1))
    return answer

# print(solution_other1(a_1, b_1))
# print(solution_other1(a_2, b_2))
# print(solution_other1(a_3, b_3))

def solution_other2(a, b):
    answer = sum(range(a,b+1) if a <= b else range(b,a+1))

    return answer

# print(solution_other2(a_1, b_1))
# print(solution_other2(a_2, b_2))
# print(solution_other2(a_3, b_3))
